import json
import urllib.parse
import urllib.request

from django.conf import settings

from .models import CallbackQuery
from .models import ChatJoinRequest
from .models import ChatMember
from .models import ChatMemberAdministrator
from .models import ChatMemberBanned
from .models import ChatMemberLeft
from .models import ChatMemberMember
from .models import ChatMemberOwner
from .models import ChatMemberRestricted
from .models import ChatMemberUpdated
from .models import ChosenInlineResult
from .models import InlineQuery
from .models import Message
from .models import Poll
from .models import PollAnswer
from .models import PreCheckoutQuery
from .models import ShippingQuery
from .models import Update

LINE_BREAK = "\n"

UPDATE_RELATED_MODELS = {
    "message": Message,
    "edited_message": Message,
    "channel_post": Message,
    "edited_channel_post": Message,
    "inline_query": InlineQuery,
    "chosen_inline_result": ChosenInlineResult,
    "callback_query": CallbackQuery,
    "shipping_query": ShippingQuery,
    "pre_checkout_query": PreCheckoutQuery,
    "poll": Poll,
    "poll_answer": PollAnswer,
    "my_chat_member": ChatMemberUpdated,
    "chat_member": ChatMemberUpdated,
    "chat_join_request": ChatJoinRequest,
}


chat_member_models = (
    ChatMemberOwner,
    ChatMemberAdministrator,
    ChatMemberMember,
    ChatMemberRestricted,
    ChatMemberLeft,
    ChatMemberBanned,
)

bot = getattr(settings, "TELEGRAM_BOT_API_KEY", None)

if bot is None:
    raise Exception("settings.TELEGRAM_BOT_API_KEY is not set")


def make_request(endpoint: str, parameters: dict):
    data = urllib.parse.urlencode(parameters)
    data = data.encode("ascii")  # data should be bytes
    request = urllib.request.Request(endpoint, data)
    try:
        with urllib.request.urlopen(request) as response:
            response_text = response.read().decode("ascii")
            status_code = response.status
    except urllib.error.HTTPError as e:
        response_text = e.read().decode("ascii")
        status_code = e.code

    return (response_text, status_code)


def get_telegram_updates():
    use_offset = getattr(settings, "TELEGRAM_USE_OFFSET_FOR_GETTING_UPDATES", True)
    base_url = f"https://api.telegram.org/bot{bot}/getUpdates"
    common_parameters = {}
    if use_offset:
        last_update_id = get_last_update_id()
        parameters = (
            {**common_parameters, "offset": last_update_id}
            if last_update_id
            else common_parameters
        )
    else:
        parameters = common_parameters
    response_text, status_code = make_request(endpoint=base_url, parameters=parameters)

    if status_code == 200:
        ok = True
        data = json.loads(response_text)
        response_dict = data["result"]

    else:
        print("There was an error getting updates. Status code: {status_code}") # TODO: improve error message
        ok = False
        response_dict = {}
    return (response_dict, ok)



def send_info_to_chat(chat_id: str, text: str):
    base_url = f"https://api.telegram.org/bot{bot}/sendMessage"
    parameters = {"chat_id": chat_id, "text": text}
    make_request(endpoint=base_url, parameters=parameters)



def create_update_objects(dict_of_updates: dict):
    update_objs = []

    for update_dict in dict_of_updates:
        just_fields_dict = update_dict
        just_related_objects_dict = {}
        for key in update_dict.copy().keys():
            related_model = getattr(Update, key).field.related_model
            if related_model:
                object_dict = _clean_object_dict(update_dict[key])
                obj = get_or_create_object(
                    object_dict, Klass=UPDATE_RELATED_MODELS[key]
                )
                just_related_objects_dict[key] = obj
                just_fields_dict.pop(key, None)

        composed_object_dict = {**just_fields_dict, **just_related_objects_dict}
        update_objs.append(Update(**composed_object_dict))
    Update.objects.bulk_create(update_objs)


def get_or_create_object(object_dict: dict, Klass):
    # Main object
    # Update children (Message, Poll, )
    just_fields_dict = object_dict
    just_related_objects_dict = {}
    for key in object_dict.copy().keys():
        key = _validate_field_name(key)
        related_model = getattr(Klass, key).field.related_model
        if related_model:
            if isinstance(object_dict[key], list):
                list_of_dicts = object_dict[key]
                value = _clean_object_dict(list_of_dicts[len(list_of_dicts) - 1])
            else:
                value = _clean_object_dict(object_dict[key])
            obj = get_or_create_related_object(object_dict=value, Klass=related_model)
            just_related_objects_dict[key] = obj
            just_fields_dict.pop(key, None)
    composed_object_dict = {**just_fields_dict, **just_related_objects_dict}
    obj, _ = Klass.objects.get_or_create(**composed_object_dict)
    return obj


def get_or_create_related_object(Klass, object_dict):
    # Related object to main object
    just_fields_dict = object_dict
    just_related_objects_dict = {}

    if not Klass == ChatMember:
        for key in object_dict.copy().keys():
            key = _validate_field_name(key)
            related_model = getattr(Klass, key).field.related_model
            if related_model:
                if isinstance(object_dict[key], list):
                    list_of_dicts = object_dict[key]
                    value = _clean_object_dict(list_of_dicts[len(list_of_dicts) - 1])
                else:
                    value = _clean_object_dict(object_dict[key])
                obj = get_or_create_subrelated_object(
                    Klass=related_model, object_dict=value
                )
                just_related_objects_dict[key] = obj
                just_fields_dict.pop(key, None)
        composed_object_dict = {**just_fields_dict, **just_related_objects_dict}
        obj, _ = Klass.objects.get_or_create(**composed_object_dict)
        return obj
    else:
        chat_member_obj_dict = {}
        for model in chat_member_models:
            set_of_model_fields = {f.name for f in model._meta.get_fields()}
            set_of_object_dict_keys = set(
                object_dict.keys() | ("chatmember", "telegram_id")
            )
            if set_of_object_dict_keys == set_of_model_fields:
                child_obj = get_or_create_subrelated_object(
                    Klass=model, object_dict=object_dict
                )
                chat_member_obj_dict[model.__name__] = child_obj
        obj = ChatMember.objects.create(**chat_member_obj_dict)
        return obj


def get_or_create_subrelated_object(Klass, object_dict):
    # Related object to "Related object to main object"
    # In other words: subrelated object
    just_fields_dict = object_dict
    just_related_objects_dict = {}
    for key in object_dict.copy().keys():
        key = _validate_field_name(key)
        related_model = getattr(Klass, key).field.related_model
        if related_model:
            if isinstance(object_dict[key], list):
                list_of_dicts = object_dict[key]
                value = _clean_object_dict(list_of_dicts[len(list_of_dicts) - 1])
            else:
                value = _clean_object_dict(object_dict[key])
            obj = get_or_create_subsubrelated_object(
                Klass=related_model, object_dict=value
            )
            just_related_objects_dict[key] = obj
            just_fields_dict.pop(key, None)
    composed_object_dict = {**just_fields_dict, **just_related_objects_dict}
    obj, _ = Klass.objects.get_or_create(**composed_object_dict)
    return obj


def get_or_create_subsubrelated_object(Klass, object_dict):
    # This object should not have related objects
    obj, _ = Klass.objects.get_or_create(**object_dict)
    return obj


# TODO: _clean_object_dict & _validate_field_name need to be combined

def _clean_object_dict(object_dict: dict):

    for key in object_dict.copy().keys():
        # empty keys -> set to None
        if object_dict[key] == []:
            object_dict[key] = None

        # "from" is "user"
        if key == "from":
            object_dict["user"] = object_dict[key]
            object_dict.pop(key, None)

        # insted of "id", we use "telegram_id"
        if key == "id":
            object_dict["telegram_id"] = object_dict[key]
            object_dict.pop(key, None)

    return object_dict


def _validate_field_name(field_name: str):
    
    if field_name == "from":
        field_name = "user"
    if field_name == "id":
        field_name = "telegram_id"
    return field_name


def get_last_update_id():
    last_obj = Update.objects.all().last()
    return getattr(last_obj, "update_id", None)
