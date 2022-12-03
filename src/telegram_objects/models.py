import auto_prefetch
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import JSONField

from . import help_text

VERY_TINY_CHAR_SIZE = 4
TINY_CHAR_SIZE = 8
VERY_SMALL_CHAR_SIZE = 16
SMALL_CHAR_SIZE = 32
MEDIUM_CHAR_SIZE = 64
BIG_CHAR_SIZE = 128
VERY_BIG_CHAR_SIZE = 256
HUGE_CHAR_SIZE = 512
VERY_HUGE_CHAR_SIZE = 1024
ENORMOUS_CHAR_SIZE = 2048
VERY_ENORMOUS_CHAR_SIZE = 4096


class Animation(models.Model):
    # This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).
    # https://core.telegram.org/bots/api#animation
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.AnimationHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.AnimationHelpText.file_unique_id,
    )
    width = models.IntegerField(
        help_text=help_text.AnimationHelpText.width,
    )
    height = models.IntegerField(
        help_text=help_text.AnimationHelpText.height,
    )
    duration = models.IntegerField(
        help_text=help_text.AnimationHelpText.duration,
    )
    thumb = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.AnimationHelpText.thumb,
    )
    file_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.AnimationHelpText.file_name,
    )
    mime_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.AnimationHelpText.mime_type,
    )
    file_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.AnimationHelpText.file_size,
    )


class Audio(models.Model):
    # This object represents an audio file to be treated as music by the Telegram clients.
    # https://core.telegram.org/bots/api#audio
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.AudioHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.AudioHelpText.file_unique_id,
    )
    duration = models.IntegerField(
        help_text=help_text.AudioHelpText.duration,
    )
    performer = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.AudioHelpText.performer,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.AudioHelpText.title,
    )
    file_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.AudioHelpText.file_name,
    )
    mime_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.AudioHelpText.mime_type,
    )
    file_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.AudioHelpText.file_size,
    )
    thumb = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.AudioHelpText.thumb,
    )


class BotCommand(models.Model):
    # This object represents a bot command.
    # https://core.telegram.org/bots/api#botcommand
    command = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.BotCommandHelpText.command,
    )
    description = models.CharField(
        max_length=VERY_BIG_CHAR_SIZE,
        help_text=help_text.BotCommandHelpText.description,
    )


class BotCommandScopeAllChatAdministrators(models.Model):
    # Represents the scope of bot commands, covering all group and supergroup chat administrators.
    # https://core.telegram.org/bots/api#botcommandscopeallchatadministrators
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.BotCommandScopeAllChatAdministratorsHelpText.type,
    )


class BotCommandScopeAllGroupChats(models.Model):
    # Represents the scope of bot commands, covering all group and supergroup chats.
    # https://core.telegram.org/bots/api#botcommandscopeallgroupchats
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.BotCommandScopeAllGroupChatsHelpText.type,
    )


class BotCommandScopeAllPrivateChats(models.Model):
    # Represents the scope of bot commands, covering all private chats.
    # https://core.telegram.org/bots/api#botcommandscopeallprivatechats
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.BotCommandScopeAllPrivateChatsHelpText.type,
    )


class BotCommandScopeChat(models.Model):
    # Represents the scope of bot commands, covering a specific chat.
    # https://core.telegram.org/bots/api#botcommandscopechat
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.BotCommandScopeChatHelpText.type,
    )
    chat_id = models.IntegerField(
        help_text=help_text.BotCommandScopeChatHelpText.chat_id,
    )


class BotCommandScopeChatAdministrators(models.Model):
    # Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
    # https://core.telegram.org/bots/api#botcommandscopechatadministrators
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.BotCommandScopeChatAdministratorsHelpText.type,
    )
    chat_id = models.IntegerField(
        help_text=help_text.BotCommandScopeChatAdministratorsHelpText.chat_id,
    )


class BotCommandScopeChatMember(models.Model):
    # Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
    # https://core.telegram.org/bots/api#botcommandscopechatmember
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.BotCommandScopeChatMemberHelpText.type,
    )
    chat_id = models.IntegerField(
        help_text=help_text.BotCommandScopeChatMemberHelpText.chat_id,
    )
    user_id = models.IntegerField(
        help_text=help_text.BotCommandScopeChatMemberHelpText.user_id,
    )


class BotCommandScopeDefault(models.Model):
    # Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope
    # are specified for the user.
    # https://core.telegram.org/bots/api#botcommandscopedefault
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.BotCommandScopeDefaultHelpText.type,
    )


class CallbackQuery(models.Model):
    # This object represents an incoming callback query from a callback button in an inline keyboard. If the
    # button that originated the query was attached to a message sent by the bot, the field message will be
    # present. If the button was attached to a message sent via the bot (in inline mode), the field
    # inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.
    # https://core.telegram.org/bots/api#callbackquery
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.CallbackQueryHelpText.telegram_id,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.CallbackQueryHelpText.user,
    )
    message = auto_prefetch.ForeignKey(
        "telegram_objects.Message",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.CallbackQueryHelpText.message,
    )
    inline_message_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.CallbackQueryHelpText.inline_message_id,
    )
    chat_instance = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.CallbackQueryHelpText.chat_instance,
    )
    data = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.CallbackQueryHelpText.data,
    )
    game_short_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.CallbackQueryHelpText.game_short_name,
    )


class Chat(models.Model):
    # This object represents a chat.
    # https://core.telegram.org/bots/api#chat
    telegram_id = models.BigIntegerField(
        help_text=help_text.ChatHelpText.telegram_id,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.ChatHelpText.type,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.title,
    )
    username = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.username,
    )
    first_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.first_name,
    )
    last_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.last_name,
    )
    is_forum = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.is_forum,
    )
    all_members_are_administrators = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.all_members_are_administrators,
    )
    photo = auto_prefetch.ForeignKey(
        "telegram_objects.ChatPhoto",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.ChatHelpText.photo,
    )
    active_usernames = ArrayField(
        models.CharField(max_length=MEDIUM_CHAR_SIZE, blank=True, null=True),
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.active_usernames,
    )
    emoji_status_custom_emoji_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.emoji_status_custom_emoji_id,
    )
    bio = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.bio,
    )
    has_private_forwards = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.has_private_forwards,
    )
    has_restricted_voice_and_video_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.has_restricted_voice_and_video_messages,
    )
    join_to_send_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.join_to_send_messages,
    )
    join_by_request = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.join_by_request,
    )
    description = models.CharField(
        max_length=VERY_BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.description,
    )
    invite_link = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.invite_link,
    )
    pinned_message = auto_prefetch.ForeignKey(
        "telegram_objects.Message",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.ChatHelpText.pinned_message,
    )
    permissions = auto_prefetch.ForeignKey(
        "telegram_objects.ChatPermissions",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.ChatHelpText.permissions,
    )
    slow_mode_delay = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.slow_mode_delay,
    )
    message_auto_delete_time = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.message_auto_delete_time,
    )
    has_protected_content = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.has_protected_content,
    )
    sticker_set_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.sticker_set_name,
    )
    can_set_sticker_set = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.can_set_sticker_set,
    )
    linked_chat_id = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.ChatHelpText.linked_chat_id,
    )
    location = auto_prefetch.ForeignKey(
        "telegram_objects.ChatLocation",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.ChatHelpText.location,
    )


class ChatAdministratorRights(models.Model):
    # Represents the rights of an administrator in a chat.
    # https://core.telegram.org/bots/api#chatadministratorrights
    is_anonymous = models.BooleanField(
        help_text=help_text.ChatAdministratorRightsHelpText.is_anonymous,
    )
    can_manage_chat = models.BooleanField(
        help_text=help_text.ChatAdministratorRightsHelpText.can_manage_chat,
    )
    can_delete_messages = models.BooleanField(
        help_text=help_text.ChatAdministratorRightsHelpText.can_delete_messages,
    )
    can_manage_video_chats = models.BooleanField(
        help_text=help_text.ChatAdministratorRightsHelpText.can_manage_video_chats,
    )
    can_restrict_members = models.BooleanField(
        help_text=help_text.ChatAdministratorRightsHelpText.can_restrict_members,
    )
    can_promote_members = models.BooleanField(
        help_text=help_text.ChatAdministratorRightsHelpText.can_promote_members,
    )
    can_change_info = models.BooleanField(
        help_text=help_text.ChatAdministratorRightsHelpText.can_change_info,
    )
    can_invite_users = models.BooleanField(
        help_text=help_text.ChatAdministratorRightsHelpText.can_invite_users,
    )
    can_post_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatAdministratorRightsHelpText.can_post_messages,
    )
    can_edit_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatAdministratorRightsHelpText.can_edit_messages,
    )
    can_pin_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatAdministratorRightsHelpText.can_pin_messages,
    )
    can_manage_topics = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatAdministratorRightsHelpText.can_manage_topics,
    )


class ChatInviteLink(models.Model):
    # Represents an invite link for a chat.
    # https://core.telegram.org/bots/api#chatinvitelink
    invite_link = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ChatInviteLinkHelpText.invite_link,
    )
    creator = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatInviteLinkHelpText.creator,
    )
    creates_join_request = models.BooleanField(
        help_text=help_text.ChatInviteLinkHelpText.creates_join_request,
    )
    is_primary = models.BooleanField(
        help_text=help_text.ChatInviteLinkHelpText.is_primary,
    )
    is_revoked = models.BooleanField(
        help_text=help_text.ChatInviteLinkHelpText.is_revoked,
    )
    name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatInviteLinkHelpText.name,
    )
    expire_date = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.ChatInviteLinkHelpText.expire_date,
    )
    member_limit = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.ChatInviteLinkHelpText.member_limit,
    )
    pending_join_request_count = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.ChatInviteLinkHelpText.pending_join_request_count,
    )


class ChatJoinRequest(models.Model):
    # Represents a join request sent to a chat.
    # https://core.telegram.org/bots/api#chatjoinrequest
    chat = auto_prefetch.ForeignKey(
        "telegram_objects.Chat",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatJoinRequestHelpText.chat,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatJoinRequestHelpText.user,
    )
    date = models.IntegerField(
        help_text=help_text.ChatJoinRequestHelpText.date,
    )
    bio = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatJoinRequestHelpText.bio,
    )
    invite_link = auto_prefetch.ForeignKey(
        "telegram_objects.ChatInviteLink",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.ChatJoinRequestHelpText.invite_link,
    )


class ChatLocation(models.Model):
    # Represents a location to which a chat is connected.
    # https://core.telegram.org/bots/api#chatlocation
    location = auto_prefetch.ForeignKey(
        "telegram_objects.Location",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatLocationHelpText.location,
    )
    address = models.CharField(
        max_length=MEDIUM_CHAR_SIZE,
        help_text=help_text.ChatLocationHelpText.address,
    )


class ChatMemberAdministrator(models.Model):
    # Represents a chat member that has some additional privileges.
    # https://core.telegram.org/bots/api#chatmemberadministrator
    status = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.ChatMemberAdministratorHelpText.status,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatMemberAdministratorHelpText.user,
    )
    can_be_edited = models.BooleanField(
        help_text=help_text.ChatMemberAdministratorHelpText.can_be_edited,
    )
    is_anonymous = models.BooleanField(
        help_text=help_text.ChatMemberAdministratorHelpText.is_anonymous,
    )
    can_manage_chat = models.BooleanField(
        help_text=help_text.ChatMemberAdministratorHelpText.can_manage_chat,
    )
    can_delete_messages = models.BooleanField(
        help_text=help_text.ChatMemberAdministratorHelpText.can_delete_messages,
    )
    can_manage_video_chats = models.BooleanField(
        help_text=help_text.ChatMemberAdministratorHelpText.can_manage_video_chats,
    )
    can_restrict_members = models.BooleanField(
        help_text=help_text.ChatMemberAdministratorHelpText.can_restrict_members,
    )
    can_promote_members = models.BooleanField(
        help_text=help_text.ChatMemberAdministratorHelpText.can_promote_members,
    )
    can_change_info = models.BooleanField(
        help_text=help_text.ChatMemberAdministratorHelpText.can_change_info,
    )
    can_invite_users = models.BooleanField(
        help_text=help_text.ChatMemberAdministratorHelpText.can_invite_users,
    )
    can_post_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatMemberAdministratorHelpText.can_post_messages,
    )
    can_edit_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatMemberAdministratorHelpText.can_edit_messages,
    )
    can_pin_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatMemberAdministratorHelpText.can_pin_messages,
    )
    can_manage_topics = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatMemberAdministratorHelpText.can_manage_topics,
    )
    custom_title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatMemberAdministratorHelpText.custom_title,
    )


class ChatMemberBanned(models.Model):
    # Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.
    # https://core.telegram.org/bots/api#chatmemberbanned
    status = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.ChatMemberBannedHelpText.status,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatMemberBannedHelpText.user,
    )
    until_date = models.IntegerField(
        help_text=help_text.ChatMemberBannedHelpText.until_date,
    )


class ChatMemberLeft(models.Model):
    # Represents a chat member that isn't currently a member of the chat, but may join it themselves.
    # https://core.telegram.org/bots/api#chatmemberleft
    status = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.ChatMemberLeftHelpText.status,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatMemberLeftHelpText.user,
    )


class ChatMemberMember(models.Model):
    # Represents a chat member that has no additional privileges or restrictions.
    # https://core.telegram.org/bots/api#chatmembermember
    status = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.ChatMemberMemberHelpText.status,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatMemberMemberHelpText.user,
    )


class ChatMemberOwner(models.Model):
    # Represents a chat member that owns the chat and has all administrator privileges.
    # https://core.telegram.org/bots/api#chatmemberowner
    status = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.ChatMemberOwnerHelpText.status,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatMemberOwnerHelpText.user,
    )
    is_anonymous = models.BooleanField(
        help_text=help_text.ChatMemberOwnerHelpText.is_anonymous,
    )
    custom_title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChatMemberOwnerHelpText.custom_title,
    )


class ChatMemberRestricted(models.Model):
    # Represents a chat member that is under certain restrictions in the chat. Supergroups only.
    # https://core.telegram.org/bots/api#chatmemberrestricted
    status = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.ChatMemberRestrictedHelpText.status,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatMemberRestrictedHelpText.user,
    )
    is_member = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.is_member,
    )
    can_change_info = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.can_change_info,
    )
    can_invite_users = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.can_invite_users,
    )
    can_pin_messages = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.can_pin_messages,
    )
    can_manage_topics = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.can_manage_topics,
    )
    can_send_messages = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.can_send_messages,
    )
    can_send_media_messages = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.can_send_media_messages,
    )
    can_send_polls = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.can_send_polls,
    )
    can_send_other_messages = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.can_send_other_messages,
    )
    can_add_web_page_previews = models.BooleanField(
        help_text=help_text.ChatMemberRestrictedHelpText.can_add_web_page_previews,
    )
    until_date = models.IntegerField(
        help_text=help_text.ChatMemberRestrictedHelpText.until_date,
    )


class ChatMemberUpdated(models.Model):
    # This object represents changes in the status of a chat member.
    # https://core.telegram.org/bots/api#chatmemberupdated
    chat = auto_prefetch.ForeignKey(
        "telegram_objects.Chat",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatMemberUpdatedHelpText.chat,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChatMemberUpdatedHelpText.user,
    )
    date = models.IntegerField(
        help_text=help_text.ChatMemberUpdatedHelpText.date,
    )
    old_chat_member = auto_prefetch.ForeignKey(
        "telegram_objects.ChatMember",
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text=help_text.ChatMemberUpdatedHelpText.old_chat_member,
    )
    new_chat_member = auto_prefetch.ForeignKey(
        "telegram_objects.ChatMember",
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text=help_text.ChatMemberUpdatedHelpText.new_chat_member,
    )
    invite_link = auto_prefetch.ForeignKey(
        "telegram_objects.ChatInviteLink",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.ChatMemberUpdatedHelpText.invite_link,
    )


class ChatPermissions(models.Model):
    # Describes actions that a non-administrator user is allowed to take in a chat.
    # https://core.telegram.org/bots/api#chatpermissions
    can_send_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatPermissionsHelpText.can_send_messages,
    )
    can_send_media_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatPermissionsHelpText.can_send_media_messages,
    )
    can_send_polls = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatPermissionsHelpText.can_send_polls,
    )
    can_send_other_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatPermissionsHelpText.can_send_other_messages,
    )
    can_add_web_page_previews = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatPermissionsHelpText.can_add_web_page_previews,
    )
    can_change_info = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatPermissionsHelpText.can_change_info,
    )
    can_invite_users = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatPermissionsHelpText.can_invite_users,
    )
    can_pin_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatPermissionsHelpText.can_pin_messages,
    )
    can_manage_topics = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ChatPermissionsHelpText.can_manage_topics,
    )


class ChatPhoto(models.Model):
    # This object represents a chat photo.
    # https://core.telegram.org/bots/api#chatphoto
    small_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ChatPhotoHelpText.small_file_id,
    )
    small_file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ChatPhotoHelpText.small_file_unique_id,
    )
    big_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ChatPhotoHelpText.big_file_id,
    )
    big_file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ChatPhotoHelpText.big_file_unique_id,
    )


class ChosenInlineResult(models.Model):
    # Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    # https://core.telegram.org/bots/api#choseninlineresult
    result_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ChosenInlineResultHelpText.result_id,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ChosenInlineResultHelpText.user,
    )
    location = auto_prefetch.ForeignKey(
        "telegram_objects.Location",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.ChosenInlineResultHelpText.location,
    )
    inline_message_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ChosenInlineResultHelpText.inline_message_id,
    )
    query = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ChosenInlineResultHelpText.query,
    )


class Contact(models.Model):
    # This object represents a phone contact.
    # https://core.telegram.org/bots/api#contact
    phone_number = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ContactHelpText.phone_number,
    )
    first_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        help_text=help_text.ContactHelpText.first_name,
    )
    last_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ContactHelpText.last_name,
    )
    user_id = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.ContactHelpText.user_id,
    )
    vcard = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ContactHelpText.vcard,
    )


class Dice(models.Model):
    # This object represents an animated emoji that displays a random value.
    # https://core.telegram.org/bots/api#dice
    emoji = models.CharField(
        max_length=1,
        help_text=help_text.DiceHelpText.emoji,
    )
    value = models.IntegerField(
        help_text=help_text.DiceHelpText.value,
    )


class Document(models.Model):
    # This object represents a general file (as opposed to photos, voice messages and audio files).
    # https://core.telegram.org/bots/api#document
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.DocumentHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.DocumentHelpText.file_unique_id,
    )
    thumb = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.DocumentHelpText.thumb,
    )
    file_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.DocumentHelpText.file_name,
    )
    mime_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.DocumentHelpText.mime_type,
    )
    file_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.DocumentHelpText.file_size,
    )


class EncryptedCredentials(models.Model):
    # Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram
    # Passport Documentation for a complete description of the data decryption and authentication processes.
    # https://core.telegram.org/bots/api#encryptedcredentials
    data = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.EncryptedCredentialsHelpText.data,
    )
    hash = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.EncryptedCredentialsHelpText.hash,
    )
    secret = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.EncryptedCredentialsHelpText.secret,
    )


class EncryptedPassportElement(models.Model):
    # Describes documents or other Telegram Passport elements shared with the bot by the user.
    # https://core.telegram.org/bots/api#encryptedpassportelement
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.EncryptedPassportElementHelpText.type,
    )
    data = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.EncryptedPassportElementHelpText.data,
    )
    phone_number = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.EncryptedPassportElementHelpText.phone_number,
    )
    email = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.EncryptedPassportElementHelpText.email,
    )
    files = auto_prefetch.ForeignKey(
        "telegram_objects.PassportFile",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.EncryptedPassportElementHelpText.files,
    )
    front_side = auto_prefetch.ForeignKey(
        "telegram_objects.PassportFile",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.EncryptedPassportElementHelpText.front_side,
    )
    reverse_side = auto_prefetch.ForeignKey(
        "telegram_objects.PassportFile",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.EncryptedPassportElementHelpText.reverse_side,
    )
    selfie = auto_prefetch.ForeignKey(
        "telegram_objects.PassportFile",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.EncryptedPassportElementHelpText.selfie,
    )
    translation = auto_prefetch.ForeignKey(
        "telegram_objects.PassportFile",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.EncryptedPassportElementHelpText.translation,
    )
    hash = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.EncryptedPassportElementHelpText.hash,
    )


class File(models.Model):
    # This object represents a file ready to be downloaded. The file can be downloaded via the link
    # https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at
    # least 1 hour. When the link expires, a new one can be requested by calling getFile.
    # https://core.telegram.org/bots/api#file
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.FileHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.FileHelpText.file_unique_id,
    )
    file_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.FileHelpText.file_size,
    )
    file_path = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.FileHelpText.file_path,
    )


class ForceReply(models.Model):
    # Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act
    # as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want
    # to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.
    # https://core.telegram.org/bots/api#forcereply
    force_reply = models.BooleanField(
        help_text=help_text.ForceReplyHelpText.force_reply,
    )
    input_field_placeholder = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ForceReplyHelpText.input_field_placeholder,
    )
    selective = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ForceReplyHelpText.selective,
    )


class ForumTopic(models.Model):
    # This object represents a forum topic.
    # https://core.telegram.org/bots/api#forumtopic
    message_thread_id = models.IntegerField(
        help_text=help_text.ForumTopicHelpText.message_thread_id,
    )
    name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        help_text=help_text.ForumTopicHelpText.name,
    )
    icon_color = models.IntegerField(
        help_text=help_text.ForumTopicHelpText.icon_color,
    )
    icon_custom_emoji_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ForumTopicHelpText.icon_custom_emoji_id,
    )


class ForumTopicCreated(models.Model):
    # This object represents a service message about a new forum topic created in the chat.
    # https://core.telegram.org/bots/api#forumtopiccreated
    name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        help_text=help_text.ForumTopicCreatedHelpText.name,
    )
    icon_color = models.IntegerField(
        help_text=help_text.ForumTopicCreatedHelpText.icon_color,
    )
    icon_custom_emoji_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ForumTopicCreatedHelpText.icon_custom_emoji_id,
    )


class Game(models.Model):
    # This object represents a game. Use BotFather to create and edit games, their short names will act as unique
    # identifiers.
    # https://core.telegram.org/bots/api#game
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.GameHelpText.title,
    )
    description = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.GameHelpText.description,
    )
    photo = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.GameHelpText.photo,
    )
    text = models.TextField(
        max_length=VERY_ENORMOUS_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.GameHelpText.text,
    )
    text_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.GameHelpText.text_entities,
    )
    animation = auto_prefetch.ForeignKey(
        "telegram_objects.Animation",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.GameHelpText.animation,
    )


class GameHighScore(models.Model):
    # This object represents one row of the high scores table for a game.
    # https://core.telegram.org/bots/api#gamehighscore
    position = models.IntegerField(
        help_text=help_text.GameHighScoreHelpText.position,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.GameHighScoreHelpText.user,
    )
    score = models.IntegerField(
        help_text=help_text.GameHighScoreHelpText.score,
    )


class InlineKeyboardButton(models.Model):
    # This object represents one button of an inline keyboard. You must use exactly one of the optional fields.
    # https://core.telegram.org/bots/api#inlinekeyboardbutton
    text = models.TextField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineKeyboardButtonHelpText.text,
    )
    url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineKeyboardButtonHelpText.url,
    )
    callback_data = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineKeyboardButtonHelpText.callback_data,
    )
    web_app = auto_prefetch.ForeignKey(
        "telegram_objects.WebAppInfo",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineKeyboardButtonHelpText.web_app,
    )
    login_url = auto_prefetch.ForeignKey(
        "telegram_objects.LoginUrl",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineKeyboardButtonHelpText.login_url,
    )
    switch_inline_query = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineKeyboardButtonHelpText.switch_inline_query,
    )
    switch_inline_query_current_chat = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineKeyboardButtonHelpText.switch_inline_query_current_chat,
    )
    callback_game = auto_prefetch.ForeignKey(
        "telegram_objects.CallbackGame",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineKeyboardButtonHelpText.callback_game,
    )
    pay = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InlineKeyboardButtonHelpText.pay,
    )


class InlineKeyboardMarkup(models.Model):
    # This object represents an inline keyboard that appears right next to the message it belongs to.
    # https://core.telegram.org/bots/api#inlinekeyboardmarkup
    inline_keyboard = JSONField(
        help_text=help_text.InlineKeyboardMarkupHelpText.inline_keyboard,
    )


class InlineQuery(models.Model):
    # This object represents an incoming inline query. When the user sends an empty query, your bot could return
    # some default or trending results.
    # https://core.telegram.org/bots/api#inlinequery
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryHelpText.telegram_id,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.InlineQueryHelpText.user,
    )
    query = models.CharField(
        max_length=VERY_BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryHelpText.query,
    )
    offset = models.CharField(
        max_length=MEDIUM_CHAR_SIZE,
        help_text=help_text.InlineQueryHelpText.offset,
    )
    chat_type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryHelpText.chat_type,
    )
    location = auto_prefetch.ForeignKey(
        "telegram_objects.Location",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryHelpText.location,
    )


class InlineQueryResultArticle(models.Model):
    # Represents a link to an article or web page.
    # https://core.telegram.org/bots/api#inlinequeryresultarticle
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultArticleHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultArticleHelpText.telegram_id,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultArticleHelpText.title,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.InlineQueryResultArticleHelpText.input_message_content,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultArticleHelpText.reply_markup,
    )
    url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultArticleHelpText.url,
    )
    hide_url = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultArticleHelpText.hide_url,
    )
    description = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultArticleHelpText.description,
    )
    thumb_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultArticleHelpText.thumb_url,
    )
    thumb_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultArticleHelpText.thumb_width,
    )
    thumb_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultArticleHelpText.thumb_height,
    )


class InlineQueryResultAudio(models.Model):
    # Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively,
    # you can use input_message_content to send a message with the specified content instead of the audio.
    # https://core.telegram.org/bots/api#inlinequeryresultaudio
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultAudioHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultAudioHelpText.telegram_id,
    )
    audio_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultAudioHelpText.audio_url,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultAudioHelpText.title,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultAudioHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultAudioHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultAudioHelpText.caption_entities,
    )
    performer = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultAudioHelpText.performer,
    )
    audio_duration = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultAudioHelpText.audio_duration,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultAudioHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultAudioHelpText.input_message_content,
    )


class InlineQueryResultCachedAudio(models.Model):
    # Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be
    # sent by the user. Alternatively, you can use input_message_content to send a message with the specified
    # content instead of the audio.
    # https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedAudioHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedAudioHelpText.telegram_id,
    )
    audio_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedAudioHelpText.audio_file_id,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedAudioHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedAudioHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedAudioHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedAudioHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedAudioHelpText.input_message_content,
    )


class InlineQueryResultCachedDocument(models.Model):
    # Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user
    # with an optional caption. Alternatively, you can use input_message_content to send a message with the
    # specified content instead of the file.
    # https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.telegram_id,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.title,
    )
    document_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.document_file_id,
    )
    description = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.description,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedDocumentHelpText.input_message_content,
    )


class InlineQueryResultCachedGif(models.Model):
    # Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file
    # will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send
    # a message with specified content instead of the animation.
    # https://core.telegram.org/bots/api#inlinequeryresultcachedgif
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedGifHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedGifHelpText.telegram_id,
    )
    gif_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedGifHelpText.gif_file_id,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedGifHelpText.title,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedGifHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedGifHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedGifHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedGifHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedGifHelpText.input_message_content,
    )


class InlineQueryResultCachedMpeg4Gif(models.Model):
    # Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram
    # servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption.
    # Alternatively, you can use input_message_content to send a message with the specified content instead of the
    # animation.
    # https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedMpeg4GifHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedMpeg4GifHelpText.telegram_id,
    )
    mpeg4_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedMpeg4GifHelpText.mpeg4_file_id,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedMpeg4GifHelpText.title,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedMpeg4GifHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedMpeg4GifHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedMpeg4GifHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedMpeg4GifHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedMpeg4GifHelpText.input_message_content,
    )


class InlineQueryResultCachedPhoto(models.Model):
    # Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user
    # with an optional caption. Alternatively, you can use input_message_content to send a message with the
    # specified content instead of the photo.
    # https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.telegram_id,
    )
    photo_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.photo_file_id,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.title,
    )
    description = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.description,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedPhotoHelpText.input_message_content,
    )


class InlineQueryResultCachedSticker(models.Model):
    # Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the
    # user. Alternatively, you can use input_message_content to send a message with the specified content instead
    # of the sticker.
    # https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedStickerHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedStickerHelpText.telegram_id,
    )
    sticker_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedStickerHelpText.sticker_file_id,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedStickerHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedStickerHelpText.input_message_content,
    )


class InlineQueryResultCachedVideo(models.Model):
    # Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent
    # by the user with an optional caption. Alternatively, you can use input_message_content to send a message
    # with the specified content instead of the video.
    # https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.telegram_id,
    )
    video_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.video_file_id,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.title,
    )
    description = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.description,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedVideoHelpText.input_message_content,
    )


class InlineQueryResultCachedVoice(models.Model):
    # Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be
    # sent by the user. Alternatively, you can use input_message_content to send a message with the specified
    # content instead of the voice message.
    # https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedVoiceHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedVoiceHelpText.telegram_id,
    )
    voice_file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedVoiceHelpText.voice_file_id,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultCachedVoiceHelpText.title,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedVoiceHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultCachedVoiceHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedVoiceHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedVoiceHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultCachedVoiceHelpText.input_message_content,
    )


class InlineQueryResultContact(models.Model):
    # Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively,
    # you can use input_message_content to send a message with the specified content instead of the contact.
    # https://core.telegram.org/bots/api#inlinequeryresultcontact
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultContactHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultContactHelpText.telegram_id,
    )
    phone_number = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultContactHelpText.phone_number,
    )
    first_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultContactHelpText.first_name,
    )
    last_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultContactHelpText.last_name,
    )
    vcard = models.CharField(
        max_length=ENORMOUS_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultContactHelpText.vcard,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultContactHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultContactHelpText.input_message_content,
    )
    thumb_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultContactHelpText.thumb_url,
    )
    thumb_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultContactHelpText.thumb_width,
    )
    thumb_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultContactHelpText.thumb_height,
    )


class InlineQueryResultDocument(models.Model):
    # Represents a link to a file. By default, this file will be sent by the user with an optional caption.
    # Alternatively, you can use input_message_content to send a message with the specified content instead of the
    # file. Currently, only .PDF and .ZIP files can be sent using this method.
    # https://core.telegram.org/bots/api#inlinequeryresultdocument
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultDocumentHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultDocumentHelpText.telegram_id,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultDocumentHelpText.title,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultDocumentHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultDocumentHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultDocumentHelpText.caption_entities,
    )
    document_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultDocumentHelpText.document_url,
    )
    mime_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultDocumentHelpText.mime_type,
    )
    description = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultDocumentHelpText.description,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultDocumentHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultDocumentHelpText.input_message_content,
    )
    thumb_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultDocumentHelpText.thumb_url,
    )
    thumb_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultDocumentHelpText.thumb_width,
    )
    thumb_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultDocumentHelpText.thumb_height,
    )


class InlineQueryResultGame(models.Model):
    # Represents a Game.
    # https://core.telegram.org/bots/api#inlinequeryresultgame
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultGameHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultGameHelpText.telegram_id,
    )
    game_short_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultGameHelpText.game_short_name,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultGameHelpText.reply_markup,
    )


class InlineQueryResultGif(models.Model):
    # Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with
    # optional caption. Alternatively, you can use input_message_content to send a message with the specified
    # content instead of the animation.
    # https://core.telegram.org/bots/api#inlinequeryresultgif
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultGifHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultGifHelpText.telegram_id,
    )
    gif_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultGifHelpText.gif_url,
    )
    gif_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultGifHelpText.gif_width,
    )
    gif_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultGifHelpText.gif_height,
    )
    gif_duration = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultGifHelpText.gif_duration,
    )
    thumb_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultGifHelpText.thumb_url,
    )
    thumb_mime_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultGifHelpText.thumb_mime_type,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultGifHelpText.title,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultGifHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultGifHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultGifHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultGifHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultGifHelpText.input_message_content,
    )


class InlineQueryResultLocation(models.Model):
    # Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can
    # use input_message_content to send a message with the specified content instead of the location.
    # https://core.telegram.org/bots/api#inlinequeryresultlocation
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultLocationHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultLocationHelpText.telegram_id,
    )
    latitude = models.BooleanField(
        help_text=help_text.InlineQueryResultLocationHelpText.latitude,
    )
    longitude = models.BooleanField(
        help_text=help_text.InlineQueryResultLocationHelpText.longitude,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultLocationHelpText.title,
    )
    horizontal_accuracy = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultLocationHelpText.horizontal_accuracy,
    )
    live_period = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultLocationHelpText.live_period,
    )
    heading = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultLocationHelpText.heading,
    )
    proximity_alert_radius = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultLocationHelpText.proximity_alert_radius,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultLocationHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultLocationHelpText.input_message_content,
    )
    thumb_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultLocationHelpText.thumb_url,
    )
    thumb_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultLocationHelpText.thumb_width,
    )
    thumb_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultLocationHelpText.thumb_height,
    )


class InlineQueryResultMpeg4Gif(models.Model):
    # Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated
    # MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content
    # to send a message with the specified content instead of the animation.
    # https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.telegram_id,
    )
    mpeg4_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.mpeg4_url,
    )
    mpeg4_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.mpeg4_width,
    )
    mpeg4_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.mpeg4_height,
    )
    mpeg4_duration = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.mpeg4_duration,
    )
    thumb_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.thumb_url,
    )
    thumb_mime_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.thumb_mime_type,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.title,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultMpeg4GifHelpText.input_message_content,
    )


class InlineQueryResultPhoto(models.Model):
    # Represents a link to a photo. By default, this photo will be sent by the user with optional caption.
    # Alternatively, you can use input_message_content to send a message with the specified content instead of the
    # photo.
    # https://core.telegram.org/bots/api#inlinequeryresultphoto
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultPhotoHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultPhotoHelpText.telegram_id,
    )
    photo_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultPhotoHelpText.photo_url,
    )
    thumb_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultPhotoHelpText.thumb_url,
    )
    photo_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultPhotoHelpText.photo_width,
    )
    photo_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultPhotoHelpText.photo_height,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultPhotoHelpText.title,
    )
    description = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultPhotoHelpText.description,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultPhotoHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultPhotoHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultPhotoHelpText.caption_entities,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultPhotoHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultPhotoHelpText.input_message_content,
    )


class InlineQueryResultVenue(models.Model):
    # Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use
    # input_message_content to send a message with the specified content instead of the venue.
    # https://core.telegram.org/bots/api#inlinequeryresultvenue
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVenueHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVenueHelpText.telegram_id,
    )
    latitude = models.BooleanField(
        help_text=help_text.InlineQueryResultVenueHelpText.latitude,
    )
    longitude = models.BooleanField(
        help_text=help_text.InlineQueryResultVenueHelpText.longitude,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVenueHelpText.title,
    )
    address = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVenueHelpText.address,
    )
    foursquare_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVenueHelpText.foursquare_id,
    )
    foursquare_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVenueHelpText.foursquare_type,
    )
    google_place_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVenueHelpText.google_place_id,
    )
    google_place_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVenueHelpText.google_place_type,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultVenueHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultVenueHelpText.input_message_content,
    )
    thumb_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVenueHelpText.thumb_url,
    )
    thumb_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVenueHelpText.thumb_width,
    )
    thumb_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVenueHelpText.thumb_height,
    )


class InlineQueryResultVideo(models.Model):
    # Represents a link to a page containing an embedded video player or a video file. By default, this video file
    # will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send
    # a message with the specified content instead of the video.
    # https://core.telegram.org/bots/api#inlinequeryresultvideo
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVideoHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVideoHelpText.telegram_id,
    )
    video_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVideoHelpText.video_url,
    )
    mime_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVideoHelpText.mime_type,
    )
    thumb_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVideoHelpText.thumb_url,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVideoHelpText.title,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVideoHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVideoHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultVideoHelpText.caption_entities,
    )
    video_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVideoHelpText.video_width,
    )
    video_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVideoHelpText.video_height,
    )
    video_duration = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVideoHelpText.video_duration,
    )
    description = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVideoHelpText.description,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultVideoHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultVideoHelpText.input_message_content,
    )


class InlineQueryResultVoice(models.Model):
    # Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice
    # recording will be sent by the user. Alternatively, you can use input_message_content to send a message with
    # the specified content instead of the the voice message.
    # https://core.telegram.org/bots/api#inlinequeryresultvoice
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVoiceHelpText.type,
    )
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVoiceHelpText.telegram_id,
    )
    voice_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVoiceHelpText.voice_url,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InlineQueryResultVoiceHelpText.title,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVoiceHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVoiceHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultVoiceHelpText.caption_entities,
    )
    voice_duration = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InlineQueryResultVoiceHelpText.voice_duration,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultVoiceHelpText.reply_markup,
    )
    input_message_content = auto_prefetch.ForeignKey(
        "telegram_objects.InputMessageContent",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InlineQueryResultVoiceHelpText.input_message_content,
    )


class InputContactMessageContent(models.Model):
    # Represents the content of a contact message to be sent as the result of an inline query.
    # https://core.telegram.org/bots/api#inputcontactmessagecontent
    phone_number = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputContactMessageContentHelpText.phone_number,
    )
    first_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        help_text=help_text.InputContactMessageContentHelpText.first_name,
    )
    last_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputContactMessageContentHelpText.last_name,
    )
    vcard = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputContactMessageContentHelpText.vcard,
    )


class InputInvoiceMessageContent(models.Model):
    # Represents the content of an invoice message to be sent as the result of an inline query.
    # https://core.telegram.org/bots/api#inputinvoicemessagecontent
    title = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        help_text=help_text.InputInvoiceMessageContentHelpText.title,
    )
    description = models.CharField(
        max_length=VERY_BIG_CHAR_SIZE,
        help_text=help_text.InputInvoiceMessageContentHelpText.description,
    )
    payload = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputInvoiceMessageContentHelpText.payload,
    )
    provider_token = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputInvoiceMessageContentHelpText.provider_token,
    )
    currency = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputInvoiceMessageContentHelpText.currency,
    )
    prices = auto_prefetch.ForeignKey(
        "telegram_objects.LabeledPrice",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.InputInvoiceMessageContentHelpText.prices,
    )
    max_tip_amount = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.max_tip_amount,
    )
    suggested_tip_amounts = ArrayField(
        models.IntegerField(blank=True, null=True),
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.suggested_tip_amounts,
    )
    provider_data = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.provider_data,
    )
    photo_url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.photo_url,
    )
    photo_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.photo_size,
    )
    photo_width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.photo_width,
    )
    photo_height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.photo_height,
    )
    need_name = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.need_name,
    )
    need_phone_number = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.need_phone_number,
    )
    need_email = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.need_email,
    )
    need_shipping_address = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.need_shipping_address,
    )
    send_phone_number_to_provider = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.send_phone_number_to_provider,
    )
    send_email_to_provider = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.send_email_to_provider,
    )
    is_flexible = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputInvoiceMessageContentHelpText.is_flexible,
    )


class InputLocationMessageContent(models.Model):
    # Represents the content of a location message to be sent as the result of an inline query.
    # https://core.telegram.org/bots/api#inputlocationmessagecontent
    latitude = models.BooleanField(
        help_text=help_text.InputLocationMessageContentHelpText.latitude,
    )
    longitude = models.BooleanField(
        help_text=help_text.InputLocationMessageContentHelpText.longitude,
    )
    horizontal_accuracy = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputLocationMessageContentHelpText.horizontal_accuracy,
    )
    live_period = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputLocationMessageContentHelpText.live_period,
    )
    heading = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputLocationMessageContentHelpText.heading,
    )
    proximity_alert_radius = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputLocationMessageContentHelpText.proximity_alert_radius,
    )


class InputMediaAnimation(models.Model):
    # Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
    # https://core.telegram.org/bots/api#inputmediaanimation
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InputMediaAnimationHelpText.type,
    )
    media = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputMediaAnimationHelpText.media,
    )
    thumb = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaAnimationHelpText.thumb,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaAnimationHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaAnimationHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InputMediaAnimationHelpText.caption_entities,
    )
    width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputMediaAnimationHelpText.width,
    )
    height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputMediaAnimationHelpText.height,
    )
    duration = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputMediaAnimationHelpText.duration,
    )


class InputMediaAudio(models.Model):
    # Represents an audio file to be treated as music to be sent.
    # https://core.telegram.org/bots/api#inputmediaaudio
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InputMediaAudioHelpText.type,
    )
    media = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputMediaAudioHelpText.media,
    )
    thumb = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaAudioHelpText.thumb,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaAudioHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaAudioHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InputMediaAudioHelpText.caption_entities,
    )
    duration = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputMediaAudioHelpText.duration,
    )
    performer = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaAudioHelpText.performer,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaAudioHelpText.title,
    )


class InputMediaDocument(models.Model):
    # Represents a general file to be sent.
    # https://core.telegram.org/bots/api#inputmediadocument
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InputMediaDocumentHelpText.type,
    )
    media = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputMediaDocumentHelpText.media,
    )
    thumb = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaDocumentHelpText.thumb,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaDocumentHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaDocumentHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InputMediaDocumentHelpText.caption_entities,
    )
    disable_content_type_detection = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputMediaDocumentHelpText.disable_content_type_detection,
    )


class InputMediaPhoto(models.Model):
    # Represents a photo to be sent.
    # https://core.telegram.org/bots/api#inputmediaphoto
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InputMediaPhotoHelpText.type,
    )
    media = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputMediaPhotoHelpText.media,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaPhotoHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaPhotoHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InputMediaPhotoHelpText.caption_entities,
    )


class InputMediaVideo(models.Model):
    # Represents a video to be sent.
    # https://core.telegram.org/bots/api#inputmediavideo
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.InputMediaVideoHelpText.type,
    )
    media = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputMediaVideoHelpText.media,
    )
    thumb = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaVideoHelpText.thumb,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaVideoHelpText.caption,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputMediaVideoHelpText.parse_mode,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InputMediaVideoHelpText.caption_entities,
    )
    width = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputMediaVideoHelpText.width,
    )
    height = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputMediaVideoHelpText.height,
    )
    duration = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.InputMediaVideoHelpText.duration,
    )
    supports_streaming = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputMediaVideoHelpText.supports_streaming,
    )


class InputTextMessageContent(models.Model):
    # Represents the content of a text message to be sent as the result of an inline query.
    # https://core.telegram.org/bots/api#inputtextmessagecontent
    message_text = models.CharField(
        max_length=VERY_ENORMOUS_CHAR_SIZE,
        help_text=help_text.InputTextMessageContentHelpText.message_text,
    )
    parse_mode = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputTextMessageContentHelpText.parse_mode,
    )
    entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.InputTextMessageContentHelpText.entities,
    )
    disable_web_page_preview = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.InputTextMessageContentHelpText.disable_web_page_preview,
    )


class InputVenueMessageContent(models.Model):
    # Represents the content of a venue message to be sent as the result of an inline query.
    # https://core.telegram.org/bots/api#inputvenuemessagecontent
    latitude = models.BooleanField(
        help_text=help_text.InputVenueMessageContentHelpText.latitude,
    )
    longitude = models.BooleanField(
        help_text=help_text.InputVenueMessageContentHelpText.longitude,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputVenueMessageContentHelpText.title,
    )
    address = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InputVenueMessageContentHelpText.address,
    )
    foursquare_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputVenueMessageContentHelpText.foursquare_id,
    )
    foursquare_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputVenueMessageContentHelpText.foursquare_type,
    )
    google_place_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputVenueMessageContentHelpText.google_place_id,
    )
    google_place_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.InputVenueMessageContentHelpText.google_place_type,
    )


class Invoice(models.Model):
    # This object contains basic information about an invoice.
    # https://core.telegram.org/bots/api#invoice
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InvoiceHelpText.title,
    )
    description = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InvoiceHelpText.description,
    )
    start_parameter = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InvoiceHelpText.start_parameter,
    )
    currency = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.InvoiceHelpText.currency,
    )
    total_amount = models.IntegerField(
        help_text=help_text.InvoiceHelpText.total_amount,
    )


class KeyboardButton(models.Model):
    # This object represents one button of the reply keyboard. For simple text buttons String can be used instead
    # of this object to specify text of the button. Optional fields web_app, request_contact, request_location,
    # and request_poll are mutually exclusive.
    # https://core.telegram.org/bots/api#keyboardbutton
    text = models.TextField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.KeyboardButtonHelpText.text,
    )
    request_contact = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.KeyboardButtonHelpText.request_contact,
    )
    request_location = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.KeyboardButtonHelpText.request_location,
    )
    request_poll = auto_prefetch.ForeignKey(
        "telegram_objects.KeyboardButtonPollType",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.KeyboardButtonHelpText.request_poll,
    )
    web_app = auto_prefetch.ForeignKey(
        "telegram_objects.WebAppInfo",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.KeyboardButtonHelpText.web_app,
    )


class KeyboardButtonPollType(models.Model):
    # This object represents type of a poll, which is allowed to be created and sent when the corresponding button
    # is pressed.
    # https://core.telegram.org/bots/api#keyboardbuttonpolltype
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.KeyboardButtonPollTypeHelpText.type,
    )


class LabeledPrice(models.Model):
    # This object represents a portion of the price for goods or services.
    # https://core.telegram.org/bots/api#labeledprice
    label = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.LabeledPriceHelpText.label,
    )
    amount = models.IntegerField(
        help_text=help_text.LabeledPriceHelpText.amount,
    )


class Location(models.Model):
    # This object represents a point on the map.
    # https://core.telegram.org/bots/api#location
    longitude = models.BooleanField(
        help_text=help_text.LocationHelpText.longitude,
    )
    latitude = models.BooleanField(
        help_text=help_text.LocationHelpText.latitude,
    )
    horizontal_accuracy = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.LocationHelpText.horizontal_accuracy,
    )
    live_period = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.LocationHelpText.live_period,
    )
    heading = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.LocationHelpText.heading,
    )
    proximity_alert_radius = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.LocationHelpText.proximity_alert_radius,
    )


class LoginUrl(models.Model):
    # This object represents a parameter of the inline keyboard button used to automatically authorize a user.
    # Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the
    # user needs to do is tap/click a button and confirm that they want to log in:
    # https://core.telegram.org/bots/api#loginurl
    url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.LoginUrlHelpText.url,
    )
    forward_text = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.LoginUrlHelpText.forward_text,
    )
    bot_username = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.LoginUrlHelpText.bot_username,
    )
    request_write_access = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.LoginUrlHelpText.request_write_access,
    )


class MaskPosition(models.Model):
    # This object describes the position on faces where a mask should be placed by default.
    # https://core.telegram.org/bots/api#maskposition
    point = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.MaskPositionHelpText.point,
    )
    x_shift = models.BooleanField(
        help_text=help_text.MaskPositionHelpText.x_shift,
    )
    y_shift = models.BooleanField(
        help_text=help_text.MaskPositionHelpText.y_shift,
    )
    scale = models.BooleanField(
        help_text=help_text.MaskPositionHelpText.scale,
    )


class MenuButtonCommands(models.Model):
    # Represents a menu button, which opens the bot's list of commands.
    # https://core.telegram.org/bots/api#menubuttoncommands
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.MenuButtonCommandsHelpText.type,
    )


class MenuButtonDefault(models.Model):
    # Describes that no specific value for the menu button was set.
    # https://core.telegram.org/bots/api#menubuttondefault
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.MenuButtonDefaultHelpText.type,
    )


class MenuButtonWebApp(models.Model):
    # Represents a menu button, which launches a Web App.
    # https://core.telegram.org/bots/api#menubuttonwebapp
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.MenuButtonWebAppHelpText.type,
    )
    text = models.TextField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.MenuButtonWebAppHelpText.text,
    )
    web_app = auto_prefetch.ForeignKey(
        "telegram_objects.WebAppInfo",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.MenuButtonWebAppHelpText.web_app,
    )


class Message(models.Model):
    # This object represents a message.
    # https://core.telegram.org/bots/api#message
    message_id = models.IntegerField(
        help_text=help_text.MessageHelpText.message_id,
    )
    message_thread_id = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.message_thread_id,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.user,
    )
    sender_chat = auto_prefetch.ForeignKey(
        "telegram_objects.Chat",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.sender_chat,
    )
    date = models.IntegerField(
        help_text=help_text.MessageHelpText.date,
    )
    chat = auto_prefetch.ForeignKey(
        "telegram_objects.Chat",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.MessageHelpText.chat,
    )
    forward_from = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.forward_from,
    )
    new_chat_participant = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    new_chat_member = auto_prefetch.ForeignKey(
        "telegram_objects.ChatMember",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    left_chat_participant = auto_prefetch.ForeignKey(
        "telegram_objects.ChatMember",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    forward_from_chat = auto_prefetch.ForeignKey(
        "telegram_objects.Chat",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.forward_from_chat,
    )
    forward_from_message_id = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.forward_from_message_id,
    )
    forward_signature = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.forward_signature,
    )
    forward_sender_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.forward_sender_name,
    )
    forward_date = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.forward_date,
    )
    is_topic_message = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.is_topic_message,
    )
    is_automatic_forward = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.is_automatic_forward,
    )
    reply_to_message = auto_prefetch.ForeignKey(
        "telegram_objects.Message",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.reply_to_message,
    )
    via_bot = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.via_bot,
    )
    edit_date = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.edit_date,
    )
    has_protected_content = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.has_protected_content,
    )
    media_group_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.media_group_id,
    )
    author_signature = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.author_signature,
    )
    text = models.TextField(
        max_length=VERY_ENORMOUS_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.text,
    )
    entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.entities,
    )
    animation = auto_prefetch.ForeignKey(
        "telegram_objects.Animation",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.animation,
    )
    audio = auto_prefetch.ForeignKey(
        "telegram_objects.Audio",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.audio,
    )
    document = auto_prefetch.ForeignKey(
        "telegram_objects.Document",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.document,
    )
    photo = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.photo,
    )
    sticker = auto_prefetch.ForeignKey(
        "telegram_objects.Sticker",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.sticker,
    )
    video = auto_prefetch.ForeignKey(
        "telegram_objects.Video",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.video,
    )
    video_note = auto_prefetch.ForeignKey(
        "telegram_objects.VideoNote",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.video_note,
    )
    voice = auto_prefetch.ForeignKey(
        "telegram_objects.Voice",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.voice,
    )
    caption = models.CharField(
        max_length=VERY_HUGE_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.caption,
    )
    caption_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.caption_entities,
    )
    contact = auto_prefetch.ForeignKey(
        "telegram_objects.Contact",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.contact,
    )
    dice = auto_prefetch.ForeignKey(
        "telegram_objects.Dice",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.dice,
    )
    game = auto_prefetch.ForeignKey(
        "telegram_objects.Game",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.game,
    )
    poll = auto_prefetch.ForeignKey(
        "telegram_objects.Poll",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.poll,
    )
    venue = auto_prefetch.ForeignKey(
        "telegram_objects.Venue",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.venue,
    )
    location = auto_prefetch.ForeignKey(
        "telegram_objects.Location",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.location,
    )
    new_chat_members = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.new_chat_members,
    )
    left_chat_member = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.left_chat_member,
    )
    new_chat_title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.new_chat_title,
    )
    new_chat_photo = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.new_chat_photo,
    )
    delete_chat_photo = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.delete_chat_photo,
    )
    group_chat_created = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.group_chat_created,
    )
    supergroup_chat_created = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.supergroup_chat_created,
    )
    channel_chat_created = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.channel_chat_created,
    )
    message_auto_delete_timer_changed = auto_prefetch.ForeignKey(
        "telegram_objects.MessageAutoDeleteTimerChanged",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.message_auto_delete_timer_changed,
    )
    migrate_to_chat_id = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.migrate_to_chat_id,
    )
    migrate_from_chat_id = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.migrate_from_chat_id,
    )
    pinned_message = auto_prefetch.ForeignKey(
        "telegram_objects.Message",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.pinned_message,
    )
    invoice = auto_prefetch.ForeignKey(
        "telegram_objects.Invoice",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.invoice,
    )
    successful_payment = auto_prefetch.ForeignKey(
        "telegram_objects.SuccessfulPayment",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.successful_payment,
    )
    connected_website = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageHelpText.connected_website,
    )
    passport_data = auto_prefetch.ForeignKey(
        "telegram_objects.PassportData",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.passport_data,
    )
    proximity_alert_triggered = auto_prefetch.ForeignKey(
        "telegram_objects.ProximityAlertTriggered",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.proximity_alert_triggered,
    )
    forum_topic_created = auto_prefetch.ForeignKey(
        "telegram_objects.ForumTopicCreated",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.forum_topic_created,
    )
    forum_topic_closed = auto_prefetch.ForeignKey(
        "telegram_objects.ForumTopicClosed",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.forum_topic_closed,
    )
    forum_topic_reopened = auto_prefetch.ForeignKey(
        "telegram_objects.ForumTopicReopened",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.forum_topic_reopened,
    )
    video_chat_scheduled = auto_prefetch.ForeignKey(
        "telegram_objects.VideoChatScheduled",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.video_chat_scheduled,
    )
    video_chat_started = auto_prefetch.ForeignKey(
        "telegram_objects.VideoChatStarted",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.video_chat_started,
    )
    video_chat_ended = auto_prefetch.ForeignKey(
        "telegram_objects.VideoChatEnded",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.video_chat_ended,
    )
    video_chat_participants_invited = auto_prefetch.ForeignKey(
        "telegram_objects.VideoChatParticipantsInvited",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.video_chat_participants_invited,
    )
    web_app_data = auto_prefetch.ForeignKey(
        "telegram_objects.WebAppData",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.web_app_data,
    )
    reply_markup = auto_prefetch.ForeignKey(
        "telegram_objects.InlineKeyboardMarkup",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageHelpText.reply_markup,
    )


class MessageAutoDeleteTimerChanged(models.Model):
    # This object represents a service message about a change in auto-delete timer settings.
    # https://core.telegram.org/bots/api#messageautodeletetimerchanged
    message_auto_delete_time = models.IntegerField(
        help_text=help_text.MessageAutoDeleteTimerChangedHelpText.message_auto_delete_time,
    )


class MessageEntity(models.Model):
    # This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.
    # https://core.telegram.org/bots/api#messageentity
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.MessageEntityHelpText.type,
    )
    offset = models.IntegerField(
        help_text=help_text.MessageEntityHelpText.offset,
    )
    length = models.IntegerField(
        help_text=help_text.MessageEntityHelpText.length,
    )
    url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageEntityHelpText.url,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.MessageEntityHelpText.user,
    )
    language = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageEntityHelpText.language,
    )
    custom_emoji_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.MessageEntityHelpText.custom_emoji_id,
    )


class MessageId(models.Model):
    # This object represents a unique message identifier.
    # https://core.telegram.org/bots/api#messageid
    message_id = models.IntegerField(
        help_text=help_text.MessageIdHelpText.message_id,
    )


class OrderInfo(models.Model):
    # This object represents information about an order.
    # https://core.telegram.org/bots/api#orderinfo
    name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.OrderInfoHelpText.name,
    )
    phone_number = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.OrderInfoHelpText.phone_number,
    )
    email = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.OrderInfoHelpText.email,
    )
    shipping_address = auto_prefetch.ForeignKey(
        "telegram_objects.ShippingAddress",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.OrderInfoHelpText.shipping_address,
    )


class PassportData(models.Model):
    # Describes Telegram Passport data shared with the bot by the user.
    # https://core.telegram.org/bots/api#passportdata
    data = auto_prefetch.ForeignKey(
        "telegram_objects.EncryptedPassportElement",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.PassportDataHelpText.data,
    )
    credentials = auto_prefetch.ForeignKey(
        "telegram_objects.EncryptedCredentials",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.PassportDataHelpText.credentials,
    )


class PassportElementErrorDataField(models.Model):
    # Represents an issue in one of the data fields that was provided by the user. The error is considered
    # resolved when the field's value changes.
    # https://core.telegram.org/bots/api#passportelementerrordatafield
    source = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorDataFieldHelpText.source,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PassportElementErrorDataFieldHelpText.type,
    )
    field_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorDataFieldHelpText.field_name,
    )
    data_hash = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorDataFieldHelpText.data_hash,
    )
    message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorDataFieldHelpText.message,
    )


class PassportElementErrorFile(models.Model):
    # Represents an issue with a document scan. The error is considered resolved when the file with the document
    # scan changes.
    # https://core.telegram.org/bots/api#passportelementerrorfile
    source = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFileHelpText.source,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFileHelpText.type,
    )
    file_hash = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFileHelpText.file_hash,
    )
    message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFileHelpText.message,
    )


class PassportElementErrorFiles(models.Model):
    # Represents an issue with a list of scans. The error is considered resolved when the list of files containing
    # the scans changes.
    # https://core.telegram.org/bots/api#passportelementerrorfiles
    source = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFilesHelpText.source,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFilesHelpText.type,
    )
    file_hashes = ArrayField(
        models.CharField(max_length=MEDIUM_CHAR_SIZE, blank=True, null=True),
        help_text=help_text.PassportElementErrorFilesHelpText.file_hashes,
    )
    message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFilesHelpText.message,
    )


class PassportElementErrorFrontSide(models.Model):
    # Represents an issue with the front side of a document. The error is considered resolved when the file with
    # the front side of the document changes.
    # https://core.telegram.org/bots/api#passportelementerrorfrontside
    source = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFrontSideHelpText.source,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFrontSideHelpText.type,
    )
    file_hash = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFrontSideHelpText.file_hash,
    )
    message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorFrontSideHelpText.message,
    )


class PassportElementErrorReverseSide(models.Model):
    # Represents an issue with the reverse side of a document. The error is considered resolved when the file with
    # reverse side of the document changes.
    # https://core.telegram.org/bots/api#passportelementerrorreverseside
    source = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorReverseSideHelpText.source,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PassportElementErrorReverseSideHelpText.type,
    )
    file_hash = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorReverseSideHelpText.file_hash,
    )
    message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorReverseSideHelpText.message,
    )


class PassportElementErrorSelfie(models.Model):
    # Represents an issue with the selfie with a document. The error is considered resolved when the file with the
    # selfie changes.
    # https://core.telegram.org/bots/api#passportelementerrorselfie
    source = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorSelfieHelpText.source,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PassportElementErrorSelfieHelpText.type,
    )
    file_hash = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorSelfieHelpText.file_hash,
    )
    message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorSelfieHelpText.message,
    )


class PassportElementErrorTranslationFile(models.Model):
    # Represents an issue with one of the files that constitute the translation of a document. The error is
    # considered resolved when the file changes.
    # https://core.telegram.org/bots/api#passportelementerrortranslationfile
    source = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorTranslationFileHelpText.source,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PassportElementErrorTranslationFileHelpText.type,
    )
    file_hash = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorTranslationFileHelpText.file_hash,
    )
    message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorTranslationFileHelpText.message,
    )


class PassportElementErrorTranslationFiles(models.Model):
    # Represents an issue with the translated version of a document. The error is considered resolved when a file
    # with the document translation change.
    # https://core.telegram.org/bots/api#passportelementerrortranslationfiles
    source = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorTranslationFilesHelpText.source,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PassportElementErrorTranslationFilesHelpText.type,
    )
    file_hashes = ArrayField(
        models.CharField(max_length=MEDIUM_CHAR_SIZE, blank=True, null=True),
        help_text=help_text.PassportElementErrorTranslationFilesHelpText.file_hashes,
    )
    message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorTranslationFilesHelpText.message,
    )


class PassportElementErrorUnspecified(models.Model):
    # Represents an issue in an unspecified place. The error is considered resolved when new data is added.
    # https://core.telegram.org/bots/api#passportelementerrorunspecified
    source = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorUnspecifiedHelpText.source,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PassportElementErrorUnspecifiedHelpText.type,
    )
    element_hash = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorUnspecifiedHelpText.element_hash,
    )
    message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportElementErrorUnspecifiedHelpText.message,
    )


class PassportFile(models.Model):
    # This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in
    # JPEG format when decrypted and don't exceed 10MB.
    # https://core.telegram.org/bots/api#passportfile
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportFileHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PassportFileHelpText.file_unique_id,
    )
    file_size = models.IntegerField(
        help_text=help_text.PassportFileHelpText.file_size,
    )
    file_date = models.IntegerField(
        help_text=help_text.PassportFileHelpText.file_date,
    )


class PhotoSize(models.Model):
    # This object represents one size of a photo or a file / sticker thumbnail.
    # https://core.telegram.org/bots/api#photosize
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PhotoSizeHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PhotoSizeHelpText.file_unique_id,
    )
    width = models.IntegerField(
        help_text=help_text.PhotoSizeHelpText.width,
    )
    height = models.IntegerField(
        help_text=help_text.PhotoSizeHelpText.height,
    )
    file_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.PhotoSizeHelpText.file_size,
    )


class Poll(models.Model):
    # This object contains information about a poll.
    # https://core.telegram.org/bots/api#poll
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PollHelpText.telegram_id,
    )
    question = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PollHelpText.question,
    )
    options = auto_prefetch.ForeignKey(
        "telegram_objects.PollOption",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.PollHelpText.options,
    )
    total_voter_count = models.IntegerField(
        help_text=help_text.PollHelpText.total_voter_count,
    )
    is_closed = models.BooleanField(
        help_text=help_text.PollHelpText.is_closed,
    )
    is_anonymous = models.BooleanField(
        help_text=help_text.PollHelpText.is_anonymous,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.PollHelpText.type,
    )
    allows_multiple_answers = models.BooleanField(
        help_text=help_text.PollHelpText.allows_multiple_answers,
    )
    correct_option_id = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.PollHelpText.correct_option_id,
    )
    explanation = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text=help_text.PollHelpText.explanation,
    )
    explanation_entities = auto_prefetch.ForeignKey(
        "telegram_objects.MessageEntity",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.PollHelpText.explanation_entities,
    )
    open_period = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.PollHelpText.open_period,
    )
    close_date = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.PollHelpText.close_date,
    )


class PollAnswer(models.Model):
    # This object represents an answer of a user in a non-anonymous poll.
    # https://core.telegram.org/bots/api#pollanswer
    poll_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PollAnswerHelpText.poll_id,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.PollAnswerHelpText.user,
    )
    option_ids = ArrayField(
        models.IntegerField(blank=True, null=True),
        help_text=help_text.PollAnswerHelpText.option_ids,
    )


class PollOption(models.Model):
    # This object contains information about one answer option in a poll.
    # https://core.telegram.org/bots/api#polloption
    text = models.TextField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PollOptionHelpText.text,
    )
    voter_count = models.IntegerField(
        help_text=help_text.PollOptionHelpText.voter_count,
    )


class PreCheckoutQuery(models.Model):
    # This object contains information about an incoming pre-checkout query.
    # https://core.telegram.org/bots/api#precheckoutquery
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PreCheckoutQueryHelpText.telegram_id,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.PreCheckoutQueryHelpText.user,
    )
    currency = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PreCheckoutQueryHelpText.currency,
    )
    total_amount = models.IntegerField(
        help_text=help_text.PreCheckoutQueryHelpText.total_amount,
    )
    invoice_payload = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.PreCheckoutQueryHelpText.invoice_payload,
    )
    shipping_option_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.PreCheckoutQueryHelpText.shipping_option_id,
    )
    order_info = auto_prefetch.ForeignKey(
        "telegram_objects.OrderInfo",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.PreCheckoutQueryHelpText.order_info,
    )


class ProximityAlertTriggered(models.Model):
    # This object represents the content of a service message, sent whenever a user in the chat triggers a
    # proximity alert set by another user.
    # https://core.telegram.org/bots/api#proximityalerttriggered
    traveler = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ProximityAlertTriggeredHelpText.traveler,
    )
    watcher = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ProximityAlertTriggeredHelpText.watcher,
    )
    distance = models.IntegerField(
        help_text=help_text.ProximityAlertTriggeredHelpText.distance,
    )


class ReplyKeyboardMarkup(models.Model):
    # This object represents a custom keyboard with reply options (see Introduction to bots for details and
    # examples).
    # https://core.telegram.org/bots/api#replykeyboardmarkup
    keyboard = JSONField(
        help_text=help_text.ReplyKeyboardMarkupHelpText.keyboard,
    )
    resize_keyboard = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ReplyKeyboardMarkupHelpText.resize_keyboard,
    )
    one_time_keyboard = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ReplyKeyboardMarkupHelpText.one_time_keyboard,
    )
    input_field_placeholder = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.ReplyKeyboardMarkupHelpText.input_field_placeholder,
    )
    selective = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ReplyKeyboardMarkupHelpText.selective,
    )


class ReplyKeyboardRemove(models.Model):
    # Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and
    # display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent
    # by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a
    # button (see ReplyKeyboardMarkup).
    # https://core.telegram.org/bots/api#replykeyboardremove
    remove_keyboard = models.BooleanField(
        help_text=help_text.ReplyKeyboardRemoveHelpText.remove_keyboard,
    )
    selective = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.ReplyKeyboardRemoveHelpText.selective,
    )


class ResponseParameters(models.Model):
    # Describes why a request was unsuccessful.
    # https://core.telegram.org/bots/api#responseparameters
    migrate_to_chat_id = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.ResponseParametersHelpText.migrate_to_chat_id,
    )
    retry_after = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.ResponseParametersHelpText.retry_after,
    )


class SentWebAppMessage(models.Model):
    # Describes an inline message sent by a Web App on behalf of a user.
    # https://core.telegram.org/bots/api#sentwebappmessage
    inline_message_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.SentWebAppMessageHelpText.inline_message_id,
    )


class ShippingAddress(models.Model):
    # This object represents a shipping address.
    # https://core.telegram.org/bots/api#shippingaddress
    country_code = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingAddressHelpText.country_code,
    )
    state = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingAddressHelpText.state,
    )
    city = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingAddressHelpText.city,
    )
    street_line1 = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingAddressHelpText.street_line1,
    )
    street_line2 = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingAddressHelpText.street_line2,
    )
    post_code = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingAddressHelpText.post_code,
    )


class ShippingOption(models.Model):
    # This object represents one shipping option.
    # https://core.telegram.org/bots/api#shippingoption
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingOptionHelpText.telegram_id,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingOptionHelpText.title,
    )
    prices = auto_prefetch.ForeignKey(
        "telegram_objects.LabeledPrice",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ShippingOptionHelpText.prices,
    )


class ShippingQuery(models.Model):
    # This object contains information about an incoming shipping query.
    # https://core.telegram.org/bots/api#shippingquery
    telegram_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingQueryHelpText.telegram_id,
    )
    user = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ShippingQueryHelpText.user,
    )
    invoice_payload = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.ShippingQueryHelpText.invoice_payload,
    )
    shipping_address = auto_prefetch.ForeignKey(
        "telegram_objects.ShippingAddress",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.ShippingQueryHelpText.shipping_address,
    )


class Sticker(models.Model):
    # This object represents a sticker.
    # https://core.telegram.org/bots/api#sticker
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.StickerHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.StickerHelpText.file_unique_id,
    )
    type = models.CharField(
        max_length=VERY_SMALL_CHAR_SIZE,
        help_text=help_text.StickerHelpText.type,
    )
    width = models.IntegerField(
        help_text=help_text.StickerHelpText.width,
    )
    height = models.IntegerField(
        help_text=help_text.StickerHelpText.height,
    )
    is_animated = models.BooleanField(
        help_text=help_text.StickerHelpText.is_animated,
    )
    is_video = models.BooleanField(
        help_text=help_text.StickerHelpText.is_video,
    )
    thumb = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.StickerHelpText.thumb,
    )
    emoji = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.StickerHelpText.emoji,
    )
    set_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.StickerHelpText.set_name,
    )
    premium_animation = auto_prefetch.ForeignKey(
        "telegram_objects.File",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.StickerHelpText.premium_animation,
    )
    mask_position = auto_prefetch.ForeignKey(
        "telegram_objects.MaskPosition",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.StickerHelpText.mask_position,
    )
    custom_emoji_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.StickerHelpText.custom_emoji_id,
    )
    file_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.StickerHelpText.file_size,
    )


class StickerSet(models.Model):
    # This object represents a sticker set.
    # https://core.telegram.org/bots/api#stickerset
    name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.StickerSetHelpText.name,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.StickerSetHelpText.title,
    )
    sticker_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.StickerSetHelpText.sticker_type,
    )
    is_animated = models.BooleanField(
        help_text=help_text.StickerSetHelpText.is_animated,
    )
    is_video = models.BooleanField(
        help_text=help_text.StickerSetHelpText.is_video,
    )
    stickers = auto_prefetch.ForeignKey(
        "telegram_objects.Sticker",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.StickerSetHelpText.stickers,
    )
    thumb = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.StickerSetHelpText.thumb,
    )


class SuccessfulPayment(models.Model):
    # This object contains basic information about a successful payment.
    # https://core.telegram.org/bots/api#successfulpayment
    currency = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.SuccessfulPaymentHelpText.currency,
    )
    total_amount = models.IntegerField(
        help_text=help_text.SuccessfulPaymentHelpText.total_amount,
    )
    invoice_payload = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.SuccessfulPaymentHelpText.invoice_payload,
    )
    shipping_option_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.SuccessfulPaymentHelpText.shipping_option_id,
    )
    order_info = auto_prefetch.ForeignKey(
        "telegram_objects.OrderInfo",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.SuccessfulPaymentHelpText.order_info,
    )
    telegram_payment_charge_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.SuccessfulPaymentHelpText.telegram_payment_charge_id,
    )
    provider_payment_charge_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.SuccessfulPaymentHelpText.provider_payment_charge_id,
    )


class Update(models.Model):
    # This object represents an incoming update.At most one of the optional parameters can be present in any given
    # update.
    # https://core.telegram.org/bots/api#update
    update_id = models.IntegerField(
        help_text=help_text.UpdateHelpText.update_id,
    )
    message = auto_prefetch.ForeignKey(
        "telegram_objects.Message",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.message,
    )
    edited_message = auto_prefetch.ForeignKey(
        "telegram_objects.Message",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.edited_message,
    )
    channel_post = auto_prefetch.ForeignKey(
        "telegram_objects.Message",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.channel_post,
    )
    edited_channel_post = auto_prefetch.ForeignKey(
        "telegram_objects.Message",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.edited_channel_post,
    )
    inline_query = auto_prefetch.ForeignKey(
        "telegram_objects.InlineQuery",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.inline_query,
    )
    chosen_inline_result = auto_prefetch.ForeignKey(
        "telegram_objects.ChosenInlineResult",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.chosen_inline_result,
    )
    callback_query = auto_prefetch.ForeignKey(
        "telegram_objects.CallbackQuery",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.callback_query,
    )
    shipping_query = auto_prefetch.ForeignKey(
        "telegram_objects.ShippingQuery",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.shipping_query,
    )
    pre_checkout_query = auto_prefetch.ForeignKey(
        "telegram_objects.PreCheckoutQuery",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.pre_checkout_query,
    )
    poll = auto_prefetch.ForeignKey(
        "telegram_objects.Poll",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.poll,
    )
    poll_answer = auto_prefetch.ForeignKey(
        "telegram_objects.PollAnswer",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.poll_answer,
    )
    my_chat_member = auto_prefetch.ForeignKey(
        "telegram_objects.ChatMemberUpdated",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.my_chat_member,
    )
    chat_member = auto_prefetch.ForeignKey(
        "telegram_objects.ChatMemberUpdated",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.chat_member,
    )
    chat_join_request = auto_prefetch.ForeignKey(
        "telegram_objects.ChatJoinRequest",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.UpdateHelpText.chat_join_request,
    )


class User(models.Model):
    # This object represents a Telegram user or bot.
    # https://core.telegram.org/bots/api#user
    telegram_id = models.BigIntegerField(
        help_text=help_text.UserHelpText.telegram_id,
    )
    is_bot = models.BooleanField(
        help_text=help_text.UserHelpText.is_bot,
    )
    first_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        help_text=help_text.UserHelpText.first_name,
    )
    last_name = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.UserHelpText.last_name,
    )
    username = models.CharField(
        max_length=SMALL_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.UserHelpText.username,
    )
    language_code = models.CharField(
        max_length=VERY_TINY_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.UserHelpText.language_code,
    )
    is_premium = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.UserHelpText.is_premium,
    )
    added_to_attachment_menu = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.UserHelpText.added_to_attachment_menu,
    )
    can_join_groups = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.UserHelpText.can_join_groups,
    )
    can_read_all_group_messages = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.UserHelpText.can_read_all_group_messages,
    )
    supports_inline_queries = models.BooleanField(
        blank=True,
        null=True,
        help_text=help_text.UserHelpText.supports_inline_queries,
    )


class UserProfilePhotos(models.Model):
    # This object represent a user's profile pictures.
    # https://core.telegram.org/bots/api#userprofilephotos
    total_count = models.IntegerField(
        help_text=help_text.UserProfilePhotosHelpText.total_count,
    )
    photos = JSONField(
        help_text=help_text.UserProfilePhotosHelpText.photos,
    )


class Venue(models.Model):
    # This object represents a venue.
    # https://core.telegram.org/bots/api#venue
    location = auto_prefetch.ForeignKey(
        "telegram_objects.Location",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.VenueHelpText.location,
    )
    title = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.VenueHelpText.title,
    )
    address = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.VenueHelpText.address,
    )
    foursquare_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.VenueHelpText.foursquare_id,
    )
    foursquare_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.VenueHelpText.foursquare_type,
    )
    google_place_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.VenueHelpText.google_place_id,
    )
    google_place_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.VenueHelpText.google_place_type,
    )


class Video(models.Model):
    # This object represents a video file.
    # https://core.telegram.org/bots/api#video
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.VideoHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.VideoHelpText.file_unique_id,
    )
    width = models.IntegerField(
        help_text=help_text.VideoHelpText.width,
    )
    height = models.IntegerField(
        help_text=help_text.VideoHelpText.height,
    )
    duration = models.IntegerField(
        help_text=help_text.VideoHelpText.duration,
    )
    thumb = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.VideoHelpText.thumb,
    )
    file_name = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.VideoHelpText.file_name,
    )
    mime_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.VideoHelpText.mime_type,
    )
    file_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.VideoHelpText.file_size,
    )


class VideoChatEnded(models.Model):
    # This object represents a service message about a video chat ended in the chat.
    # https://core.telegram.org/bots/api#videochatended
    duration = models.IntegerField(
        help_text=help_text.VideoChatEndedHelpText.duration,
    )


class VideoChatParticipantsInvited(models.Model):
    # This object represents a service message about new members invited to a video chat.
    # https://core.telegram.org/bots/api#videochatparticipantsinvited
    users = auto_prefetch.ForeignKey(
        "telegram_objects.User",
        related_name="+",
        on_delete=models.CASCADE,
        help_text=help_text.VideoChatParticipantsInvitedHelpText.users,
    )


class VideoChatScheduled(models.Model):
    # This object represents a service message about a video chat scheduled in the chat.
    # https://core.telegram.org/bots/api#videochatscheduled
    start_date = models.IntegerField(
        help_text=help_text.VideoChatScheduledHelpText.start_date,
    )


class VideoNote(models.Model):
    # This object represents a video message (available in Telegram apps as of v.4.0).
    # https://core.telegram.org/bots/api#videonote
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.VideoNoteHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.VideoNoteHelpText.file_unique_id,
    )
    length = models.IntegerField(
        help_text=help_text.VideoNoteHelpText.length,
    )
    duration = models.IntegerField(
        help_text=help_text.VideoNoteHelpText.duration,
    )
    thumb = auto_prefetch.ForeignKey(
        "telegram_objects.PhotoSize",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=help_text.VideoNoteHelpText.thumb,
    )
    file_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.VideoNoteHelpText.file_size,
    )


class Voice(models.Model):
    # This object represents a voice note.
    # https://core.telegram.org/bots/api#voice
    file_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.VoiceHelpText.file_id,
    )
    file_unique_id = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.VoiceHelpText.file_unique_id,
    )
    duration = models.IntegerField(
        help_text=help_text.VoiceHelpText.duration,
    )
    mime_type = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.VoiceHelpText.mime_type,
    )
    file_size = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.VoiceHelpText.file_size,
    )


class WebAppData(models.Model):
    # Describes data sent from a Web App to the bot.
    # https://core.telegram.org/bots/api#webappdata
    data = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.WebAppDataHelpText.data,
    )
    button_text = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.WebAppDataHelpText.button_text,
    )


class WebAppInfo(models.Model):
    # Describes a Web App.
    # https://core.telegram.org/bots/api#webappinfo
    url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.WebAppInfoHelpText.url,
    )


class WebhookInfo(models.Model):
    # Describes the current status of a webhook.
    # https://core.telegram.org/bots/api#webhookinfo
    url = models.CharField(
        max_length=BIG_CHAR_SIZE,
        help_text=help_text.WebhookInfoHelpText.url,
    )
    has_custom_certificate = models.BooleanField(
        help_text=help_text.WebhookInfoHelpText.has_custom_certificate,
    )
    pending_update_count = models.IntegerField(
        help_text=help_text.WebhookInfoHelpText.pending_update_count,
    )
    ip_address = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.WebhookInfoHelpText.ip_address,
    )
    last_error_date = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.WebhookInfoHelpText.last_error_date,
    )
    last_error_message = models.CharField(
        max_length=BIG_CHAR_SIZE,
        blank=True,
        null=True,
        help_text=help_text.WebhookInfoHelpText.last_error_message,
    )
    last_synchronization_error_date = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.WebhookInfoHelpText.last_synchronization_error_date,
    )
    max_connections = models.IntegerField(
        blank=True,
        null=True,
        help_text=help_text.WebhookInfoHelpText.max_connections,
    )
    allowed_updates = ArrayField(
        models.CharField(max_length=MEDIUM_CHAR_SIZE, blank=True, null=True),
        blank=True,
        null=True,
        help_text=help_text.WebhookInfoHelpText.allowed_updates,
    )


class ChatMember(models.Model):
    # This object contains information about one member of a chat. Currently, the following 6 types of chat
    # members are supported:
    # https://core.telegram.org/bots/api#chatmember
    ChatMemberOwner = auto_prefetch.OneToOneField(
        "telegram_objects.ChatMemberOwner", null=True, blank=True, on_delete=models.SET_NULL
    )
    ChatMemberAdministrator = auto_prefetch.OneToOneField(
        "telegram_objects.ChatMemberAdministrator", null=True, blank=True, on_delete=models.SET_NULL
    )
    ChatMemberMember = auto_prefetch.OneToOneField(
        "telegram_objects.ChatMemberMember", null=True, blank=True, on_delete=models.SET_NULL
    )
    ChatMemberRestricted = auto_prefetch.OneToOneField(
        "telegram_objects.ChatMemberRestricted", null=True, blank=True, on_delete=models.SET_NULL
    )
    ChatMemberLeft = auto_prefetch.OneToOneField(
        "telegram_objects.ChatMemberLeft", null=True, blank=True, on_delete=models.SET_NULL
    )
    ChatMemberBanned = auto_prefetch.OneToOneField(
        "telegram_objects.ChatMemberBanned", null=True, blank=True, on_delete=models.SET_NULL
    )


class InputMessageContent(models.Model):
    # This object represents the content of a message to be sent as a result of an inline query. Telegram clients
    # currently support the following 5 types:
    # https://core.telegram.org/bots/api#inputmessagecontent
    InputTextMessageContent = auto_prefetch.OneToOneField(
        "telegram_objects.InputTextMessageContent", null=True, blank=True, on_delete=models.SET_NULL
    )
    InputLocationMessageContent = auto_prefetch.OneToOneField(
        "telegram_objects.InputLocationMessageContent",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    InputVenueMessageContent = auto_prefetch.OneToOneField(
        "telegram_objects.InputVenueMessageContent",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    InputContactMessageContent = auto_prefetch.OneToOneField(
        "telegram_objects.InputContactMessageContent",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    InputInvoiceMessageContent = auto_prefetch.OneToOneField(
        "telegram_objects.InputInvoiceMessageContent",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )


class CallbackGame(models.Model):
    # A placeholder, currently holds no information. Use BotFather to set up your game.
    # https://core.telegram.org/bots/api#callbackgame
    pass


class ForumTopicClosed(models.Model):
    # This object represents a service message about a forum topic closed in the chat. Currently holds no
    # information.
    # https://core.telegram.org/bots/api#forumtopicclosed
    pass


class ForumTopicReopened(models.Model):
    # This object represents a service message about a forum topic reopened in the chat. Currently holds no
    # information.
    # https://core.telegram.org/bots/api#forumtopicreopened
    pass


class VideoChatStarted(models.Model):
    # This object represents a service message about a video chat started in the chat. Currently holds no
    # information.
    # https://core.telegram.org/bots/api#videochatstarted
    pass
