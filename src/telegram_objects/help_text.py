from django.utils.translation import gettext as _


class AnimationHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    width = _("""Video width as defined by sender""")
    height = _("""Video height as defined by sender""")
    duration = _("""Duration of the video in seconds as defined by sender""")
    thumb = _("""Optional. Animation thumbnail as defined by sender""")
    file_name = _("""Optional. Original animation filename as defined by sender""")
    mime_type = _("""Optional. MIME type of the file as defined by sender""")
    file_size = _(
        """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may
        have difficulty/silent defects in interpreting it. But it has at most 52 significant
        bits, so a signed 64-bit integer or double-precision float type are safe for storing
        this value."""
    )


class AudioHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    duration = _("""Duration of the audio in seconds as defined by sender""")
    performer = _(
        """Optional. Performer of the audio as defined by sender or by audio tags"""
    )
    title = _("""Optional. Title of the audio as defined by sender or by audio tags""")
    file_name = _("""Optional. Original filename as defined by sender""")
    mime_type = _("""Optional. MIME type of the file as defined by sender""")
    file_size = _(
        """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may
        have difficulty/silent defects in interpreting it. But it has at most 52 significant
        bits, so a signed 64-bit integer or double-precision float type are safe for storing
        this value."""
    )
    thumb = _(
        """Optional. Thumbnail of the album cover to which the music file belongs"""
    )


class BotCommandHelpText:
    command = _(
        """Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and
        underscores."""
    )
    description = _("""Description of the command; 1-256 characters.""")


class BotCommandScopeAllChatAdministratorsHelpText:
    type = _("""Scope type, must be all_chat_administrators""")


class BotCommandScopeAllGroupChatsHelpText:
    type = _("""Scope type, must be all_group_chats""")


class BotCommandScopeAllPrivateChatsHelpText:
    type = _("""Scope type, must be all_private_chats""")


class BotCommandScopeChatHelpText:
    type = _("""Scope type, must be chat""")
    chat_id = _(
        """Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername)"""
    )


class BotCommandScopeChatAdministratorsHelpText:
    type = _("""Scope type, must be chat_administrators""")
    chat_id = _(
        """Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername)"""
    )


class BotCommandScopeChatMemberHelpText:
    type = _("""Scope type, must be chat_member""")
    chat_id = _(
        """Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername)"""
    )
    user_id = _("""Unique identifier of the target user""")


class BotCommandScopeDefaultHelpText:
    type = _("""Scope type, must be default""")


class CallbackQueryHelpText:
    telegram_id = _("""Unique identifier for this query""")
    user = _("""Sender""")
    message = _(
        """Optional. Message with the callback button that originated the query. Note that message content
        and message date will not be available if the message is too old"""
    )
    inline_message_id = _(
        """Optional. Identifier of the message sent via the bot in inline mode, that originated
        the query."""
    )
    chat_instance = _(
        """Global identifier, uniquely corresponding to the chat to which the message with the
        callback button was sent. Useful for high scores in games."""
    )
    data = _(
        """Optional. Data associated with the callback button. Be aware that the message originated the query
        can contain no callback buttons with this data."""
    )
    game_short_name = _(
        """Optional. Short name of a Game to be returned, serves as the unique identifier for the
        game"""
    )


class ChatHelpText:
    telegram_id = _(
        """Unique identifier for this chat. This number may have more than 32 significant bits and some
        programming languages may have difficulty/silent defects in interpreting it. But it
        has at most 52 significant bits, so a signed 64-bit integer or double-precision
        float type are safe for storing this identifier."""
    )
    type = _(
        """Type of chat, can be either “private”, “group”, “supergroup” or “channel”"""
    )
    title = _("""Optional. Title, for supergroups, channels and group chats""")
    username = _(
        """Optional. Username, for private chats, supergroups and channels if available"""
    )
    first_name = _("""Optional. First name of the other party in a private chat""")
    last_name = _("""Optional. Last name of the other party in a private chat""")
    is_forum = _(
        """Optional. True, if the supergroup chat is a forum (has topics enabled)"""
    )
    photo = _("""Optional. Chat photo. Returned only in getChat.""")
    active_usernames = _(
        """Optional. If non-empty, the list of all active chat usernames; for private chats,
        supergroups and channels. Returned only in getChat."""
    )
    all_members_are_administrators = _(
        """Optional. True, if all the members of the chat object are administrators"""
    )
    emoji_status_custom_emoji_id = _(
        """Optional. Custom emoji identifier of emoji status of the other party in a
        private chat. Returned only in getChat."""
    )
    bio = _(
        """Optional. Bio of the other party in a private chat. Returned only in getChat."""
    )
    has_private_forwards = _(
        """Optional. True, if privacy settings of the other party in the private chat allows
        to use tg://user?id=<user_id> links only in chats with the user. Returned
        only in getChat."""
    )
    has_restricted_voice_and_video_messages = _(
        """Optional. True, if the privacy settings of the other party
        restrict sending voice and video note messages in the
        private chat. Returned only in getChat."""
    )
    join_to_send_messages = _(
        """Optional. True, if users need to join the supergroup before they can send
        messages. Returned only in getChat."""
    )
    join_by_request = _(
        """Optional. True, if all users directly joining the supergroup need to be approved by
        supergroup administrators. Returned only in getChat."""
    )
    description = _(
        """Optional. Description, for groups, supergroups and channel chats. Returned only in getChat."""
    )
    invite_link = _(
        """Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in
        getChat."""
    )
    pinned_message = _(
        """Optional. The most recent pinned message (by sending date). Returned only in getChat."""
    )
    permissions = _(
        """Optional. Default chat member permissions, for groups and supergroups. Returned only in
        getChat."""
    )
    slow_mode_delay = _(
        """Optional. For supergroups, the minimum allowed delay between consecutive messages sent
        by each unpriviledged user; in seconds. Returned only in getChat."""
    )
    message_auto_delete_time = _(
        """Optional. The time after which all messages sent to the chat will be
        automatically deleted; in seconds. Returned only in getChat."""
    )
    has_protected_content = _(
        """Optional. True, if messages from the chat can't be forwarded to other chats.
        Returned only in getChat."""
    )
    sticker_set_name = _(
        """Optional. For supergroups, name of group sticker set. Returned only in getChat."""
    )
    can_set_sticker_set = _(
        """Optional. True, if the bot can change the group sticker set. Returned only in
        getChat."""
    )
    linked_chat_id = _(
        """Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for
        a channel and vice versa; for supergroups and channel chats. This identifier may
        be greater than 32 bits and some programming languages may have difficulty/silent
        defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit
        integer or double-precision float type are safe for storing this identifier.
        Returned only in getChat."""
    )
    location = _(
        """Optional. For supergroups, the location to which the supergroup is connected. Returned only in
        getChat."""
    )


class ChatAdministratorRightsHelpText:
    is_anonymous = _("""True, if the user's presence in the chat is hidden""")
    can_manage_chat = _(
        """True, if the administrator can access the chat event log, chat statistics, message
        statistics in channels, see channel members, see anonymous administrators in
        supergroups and ignore slow mode. Implied by any other administrator privilege"""
    )
    can_delete_messages = _(
        """True, if the administrator can delete messages of other users"""
    )
    can_manage_video_chats = _("""True, if the administrator can manage video chats""")
    can_restrict_members = _(
        """True, if the administrator can restrict, ban or unban chat members"""
    )
    can_promote_members = _(
        """True, if the administrator can add new administrators with a subset of their own
        privileges or demote administrators that he has promoted, directly or
        indirectly (promoted by administrators that were appointed by the user)"""
    )
    can_change_info = _(
        """True, if the user is allowed to change the chat title, photo and other settings"""
    )
    can_invite_users = _(
        """True, if the user is allowed to invite new users to the chat"""
    )
    can_post_messages = _(
        """Optional. True, if the administrator can post in the channel; channels only"""
    )
    can_edit_messages = _(
        """Optional. True, if the administrator can edit messages of other users and can pin
        messages; channels only"""
    )
    can_pin_messages = _(
        """Optional. True, if the user is allowed to pin messages; groups and supergroups only"""
    )
    can_manage_topics = _(
        """Optional. True, if the user is allowed to create, rename, close, and reopen forum
        topics; supergroups only"""
    )


class ChatInviteLinkHelpText:
    invite_link = _(
        """The invite link. If the link was created by another chat administrator, then the second part
        of the link will be replaced with “…”."""
    )
    creator = _("""Creator of the link""")
    creates_join_request = _(
        """True, if users joining the chat via the link need to be approved by chat
        administrators"""
    )
    is_primary = _("""True, if the link is primary""")
    is_revoked = _("""True, if the link is revoked""")
    name = _("""Optional. Invite link name""")
    expire_date = _(
        """Optional. Point in time (Unix timestamp) when the link will expire or has been expired"""
    )
    member_limit = _(
        """Optional. The maximum number of users that can be members of the chat simultaneously after
        joining the chat via this invite link; 1-99999"""
    )
    pending_join_request_count = _(
        """Optional. Number of pending join requests created using this link"""
    )


class ChatJoinRequestHelpText:
    chat = _("""Chat to which the request was sent""")
    user = _("""User that sent the join request""")
    date = _("""Date the request was sent in Unix time""")
    bio = _("""Optional. Bio of the user.""")
    invite_link = _(
        """Optional. Chat invite link that was used by the user to send the join request"""
    )


class ChatLocationHelpText:
    location = _(
        """The location to which the supergroup is connected. Can't be a live location."""
    )
    address = _("""Location address; 1-64 characters, as defined by the chat owner""")


class ChatMemberAdministratorHelpText:
    status = _("""The member's status in the chat, always “administrator”""")
    user = _("""Information about the user""")
    can_be_edited = _(
        """True, if the bot is allowed to edit administrator privileges of that user"""
    )
    is_anonymous = _("""True, if the user's presence in the chat is hidden""")
    can_manage_chat = _(
        """True, if the administrator can access the chat event log, chat statistics, message
        statistics in channels, see channel members, see anonymous administrators in
        supergroups and ignore slow mode. Implied by any other administrator privilege"""
    )
    can_delete_messages = _(
        """True, if the administrator can delete messages of other users"""
    )
    can_manage_video_chats = _("""True, if the administrator can manage video chats""")
    can_restrict_members = _(
        """True, if the administrator can restrict, ban or unban chat members"""
    )
    can_promote_members = _(
        """True, if the administrator can add new administrators with a subset of their own
        privileges or demote administrators that he has promoted, directly or
        indirectly (promoted by administrators that were appointed by the user)"""
    )
    can_change_info = _(
        """True, if the user is allowed to change the chat title, photo and other settings"""
    )
    can_invite_users = _(
        """True, if the user is allowed to invite new users to the chat"""
    )
    can_post_messages = _(
        """Optional. True, if the administrator can post in the channel; channels only"""
    )
    can_edit_messages = _(
        """Optional. True, if the administrator can edit messages of other users and can pin
        messages; channels only"""
    )
    can_pin_messages = _(
        """Optional. True, if the user is allowed to pin messages; groups and supergroups only"""
    )
    can_manage_topics = _(
        """Optional. True, if the user is allowed to create, rename, close, and reopen forum
        topics; supergroups only"""
    )
    custom_title = _("""Optional. Custom title for this user""")


class ChatMemberBannedHelpText:
    status = _("""The member's status in the chat, always “kicked”""")
    user = _("""Information about the user""")
    until_date = _(
        """Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned
        forever"""
    )


class ChatMemberLeftHelpText:
    status = _("""The member's status in the chat, always “left”""")
    user = _("""Information about the user""")


class ChatMemberMemberHelpText:
    status = _("""The member's status in the chat, always “member”""")
    user = _("""Information about the user""")


class ChatMemberOwnerHelpText:
    status = _("""The member's status in the chat, always “creator”""")
    user = _("""Information about the user""")
    is_anonymous = _("""True, if the user's presence in the chat is hidden""")
    custom_title = _("""Optional. Custom title for this user""")


class ChatMemberRestrictedHelpText:
    status = _("""The member's status in the chat, always “restricted”""")
    user = _("""Information about the user""")
    is_member = _(
        """True, if the user is a member of the chat at the moment of the request"""
    )
    can_change_info = _(
        """True, if the user is allowed to change the chat title, photo and other settings"""
    )
    can_invite_users = _(
        """True, if the user is allowed to invite new users to the chat"""
    )
    can_pin_messages = _("""True, if the user is allowed to pin messages""")
    can_manage_topics = _("""True, if the user is allowed to create forum topics""")
    can_send_messages = _(
        """True, if the user is allowed to send text messages, contacts, locations and venues"""
    )
    can_send_media_messages = _(
        """True, if the user is allowed to send audios, documents, photos, videos, video
        notes and voice notes"""
    )
    can_send_polls = _("""True, if the user is allowed to send polls""")
    can_send_other_messages = _(
        """True, if the user is allowed to send animations, games, stickers and use inline
        bots"""
    )
    can_add_web_page_previews = _(
        """True, if the user is allowed to add web page previews to their messages"""
    )
    until_date = _(
        """Date when restrictions will be lifted for this user; unix time. If 0, then the user is
        restricted forever"""
    )


class ChatMemberUpdatedHelpText:
    chat = _("""Chat the user belongs to""")
    user = _("""Performer of the action, which resulted in the change""")
    date = _("""Date the change was done in Unix time""")
    old_chat_member = _("""Previous information about the chat member""")
    new_chat_member = _("""New information about the chat member""")
    invite_link = _(
        """Optional. Chat invite link, which was used by the user to join the chat; for joining by
        invite link events only."""
    )


class ChatPermissionsHelpText:
    can_send_messages = _(
        """Optional. True, if the user is allowed to send text messages, contacts, locations and
        venues"""
    )
    can_send_media_messages = _(
        """Optional. True, if the user is allowed to send audios, documents, photos,
        videos, video notes and voice notes, implies can_send_messages"""
    )
    can_send_polls = _(
        """Optional. True, if the user is allowed to send polls, implies can_send_messages"""
    )
    can_send_other_messages = _(
        """Optional. True, if the user is allowed to send animations, games, stickers and
        use inline bots, implies can_send_media_messages"""
    )
    can_add_web_page_previews = _(
        """Optional. True, if the user is allowed to add web page previews to their
        messages, implies can_send_media_messages"""
    )
    can_change_info = _(
        """Optional. True, if the user is allowed to change the chat title, photo and other
        settings. Ignored in public supergroups"""
    )
    can_invite_users = _(
        """Optional. True, if the user is allowed to invite new users to the chat"""
    )
    can_pin_messages = _(
        """Optional. True, if the user is allowed to pin messages. Ignored in public supergroups"""
    )
    can_manage_topics = _(
        """Optional. True, if the user is allowed to create forum topics. If omitted defaults to
        the value of can_pin_messages"""
    )


class ChatPhotoHelpText:
    small_file_id = _(
        """File identifier of small (160x160) chat photo. This file_id can be used only for photo
        download and only for as long as the photo is not changed."""
    )
    small_file_unique_id = _(
        """Unique file identifier of small (160x160) chat photo, which is supposed to be the
        same over time and for different bots. Can't be used to download or reuse
        the file."""
    )
    big_file_id = _(
        """File identifier of big (640x640) chat photo. This file_id can be used only for photo
        download and only for as long as the photo is not changed."""
    )
    big_file_unique_id = _(
        """Unique file identifier of big (640x640) chat photo, which is supposed to be the same
        over time and for different bots. Can't be used to download or reuse the
        file."""
    )


class ChosenInlineResultHelpText:
    result_id = _("""The unique identifier for the result that was chosen""")
    user = _("""The user that chose the result""")
    location = _(
        """Optional. Sender location, only for bots that require user location"""
    )
    inline_message_id = _(
        """Optional. Identifier of the sent inline message. Available only if there is an inline
        keyboard attached to the message. Will be also received in callback queries
        and can be used to edit the message."""
    )
    query = _("""The query that was used to obtain the result""")


class ContactHelpText:
    phone_number = _("""Contact's phone number""")
    first_name = _("""Contact's first name""")
    last_name = _("""Optional. Contact's last name""")
    user_id = _(
        """Optional. Contact's user identifier in Telegram. This number may have more than 32 significant
        bits and some programming languages may have difficulty/silent defects in interpreting
        it. But it has at most 52 significant bits, so a 64-bit integer or double-precision
        float type are safe for storing this identifier."""
    )
    vcard = _("""Optional. Additional data about the contact in the form of a vCard""")


class DiceHelpText:
    emoji = _("""Emoji on which the dice throw animation is based""")
    value = _(
        """Value of the dice, 1-6 for “”, “” and “” base emoji, 1-5 for “” and “” base emoji, 1-64 for “”
        base emoji"""
    )


class DocumentHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    thumb = _("""Optional. Document thumbnail as defined by sender""")
    file_name = _("""Optional. Original filename as defined by sender""")
    mime_type = _("""Optional. MIME type of the file as defined by sender""")
    file_size = _(
        """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may
        have difficulty/silent defects in interpreting it. But it has at most 52 significant
        bits, so a signed 64-bit integer or double-precision float type are safe for storing
        this value."""
    )


class EncryptedCredentialsHelpText:
    data = _(
        """Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets
        required for EncryptedPassportElement decryption and authentication"""
    )
    hash = _("""Base64-encoded data hash for data authentication""")
    secret = _(
        """Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption"""
    )


class EncryptedPassportElementHelpText:
    type = _(
        """Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”,
        “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”,
        “passport_registration”, “temporary_registration”, “phone_number”, “email”."""
    )
    data = _(
        """Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available
        for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”
        and “address” types. Can be decrypted and verified using the accompanying
        EncryptedCredentials."""
    )
    phone_number = _(
        """Optional. User's verified phone number, available only for “phone_number” type"""
    )
    email = _(
        """Optional. User's verified email address, available only for “email” type"""
    )
    files = _(
        """Optional. Array of encrypted files with documents provided by the user, available for
        “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and
        “temporary_registration” types. Files can be decrypted and verified using the accompanying
        EncryptedCredentials."""
    )
    front_side = _(
        """Optional. Encrypted file with the front side of the document, provided by the user. Available
        for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file
        can be decrypted and verified using the accompanying EncryptedCredentials."""
    )
    reverse_side = _(
        """Optional. Encrypted file with the reverse side of the document, provided by the user.
        Available for “driver_license” and “identity_card”. The file can be decrypted and
        verified using the accompanying EncryptedCredentials."""
    )
    selfie = _(
        """Optional. Encrypted file with the selfie of the user holding a document, provided by the user;
        available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The
        file can be decrypted and verified using the accompanying EncryptedCredentials."""
    )
    translation = _(
        """Optional. Array of encrypted files with translated versions of documents provided by the
        user. Available if requested for “passport”, “driver_license”, “identity_card”,
        “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”,
        “passport_registration” and “temporary_registration” types. Files can be decrypted
        and verified using the accompanying EncryptedCredentials."""
    )
    hash = _(
        """Base64-encoded element hash for using in PassportElementErrorUnspecified"""
    )


class FileHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    file_size = _(
        """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may
        have difficulty/silent defects in interpreting it. But it has at most 52 significant
        bits, so a signed 64-bit integer or double-precision float type are safe for storing
        this value."""
    )
    file_path = _(
        """Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file."""
    )


class ForceReplyHelpText:
    force_reply = _(
        """Shows reply interface to the user, as if they manually selected the bot's message and tapped
        'Reply'"""
    )
    input_field_placeholder = _(
        """Optional. The placeholder to be shown in the input field when the reply is
        active; 1-64 characters"""
    )
    selective = _(
        """Optional. Use this parameter if you want to force reply from specific users only. Targets: 1)
        users that are @mentioned in the text of the Message object; 2) if the bot's message
        is a reply (has reply_to_message_id), sender of the original message."""
    )


class ForumTopicHelpText:
    message_thread_id = _("""Unique identifier of the forum topic""")
    name = _("""Name of the topic""")
    icon_color = _("""Color of the topic icon in RGB format""")
    icon_custom_emoji_id = _(
        """Optional. Unique identifier of the custom emoji shown as the topic icon"""
    )


class ForumTopicCreatedHelpText:
    name = _("""Name of the topic""")
    icon_color = _("""Color of the topic icon in RGB format""")
    icon_custom_emoji_id = _(
        """Optional. Unique identifier of the custom emoji shown as the topic icon"""
    )


class GameHelpText:
    title = _("""Title of the game""")
    description = _("""Description of the game""")
    photo = _("""Photo that will be displayed in the game message in chats.""")
    text = _(
        """Optional. Brief description of the game or high scores included in the game message. Can be
        automatically edited to include current high scores for the game when the bot calls
        setGameScore, or manually edited using editMessageText. 0-4096 characters."""
    )
    text_entities = _(
        """Optional. Special entities that appear in text, such as usernames, URLs, bot commands,
        etc."""
    )
    animation = _(
        """Optional. Animation that will be displayed in the game message in chats. Upload via BotFather"""
    )


class GameHighScoreHelpText:
    position = _("""Position in high score table for the game""")
    user = _("""User""")
    score = _("""Score""")


class InlineKeyboardButtonHelpText:
    text = _("""Label text on the button""")
    url = _(
        """Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id>
        can be used to mention a user by their ID without using a username, if this is allowed by
        their privacy settings."""
    )
    callback_data = _(
        """Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64
        bytes"""
    )
    web_app = _(
        """Optional. Description of the Web App that will be launched when the user presses the button. The
        Web App will be able to send an arbitrary message on behalf of the user using the method
        answerWebAppQuery. Available only in private chats between a user and the bot."""
    )
    login_url = _(
        """Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement
        for the Telegram Login Widget."""
    )
    switch_inline_query = _(
        """Optional. If set, pressing the button will prompt the user to select one of their
        chats, open that chat and insert the bot's username and the specified inline
        query in the input field. May be empty, in which case just the bot's
        username will be inserted.Note: This offers an easy way for users to start
        using your bot in inline mode when they are currently in a private chat with
        it. Especially useful when combined with switch_pm… actions - in this case
        the user will be automatically returned to the chat they switched from,
        skipping the chat selection screen."""
    )
    switch_inline_query_current_chat = _(
        """Optional. If set, pressing the button will insert the bot's username
        and the specified inline query in the current chat's input
        field. May be empty, in which case only the bot's username will
        be inserted.This offers a quick way for the user to open your
        bot in inline mode in the same chat - good for selecting
        something from multiple options."""
    )
    callback_game = _(
        """Optional. Description of the game that will be launched when the user presses the
        button.NOTE: This type of button must always be the first button in the first row."""
    )
    pay = _(
        """Optional. Specify True, to send a Pay button.NOTE: This type of button must always be the first
        button in the first row and can only be used in invoice messages."""
    )


class InlineKeyboardMarkupHelpText:
    inline_keyboard = _(
        """Array of button rows, each represented by an Array of InlineKeyboardButton objects"""
    )


class InlineQueryHelpText:
    telegram_id = _("""Unique identifier for this query""")
    user = _("""Sender""")
    query = _("""Text of the query (up to 256 characters)""")
    offset = _("""Offset of the results to be returned, can be controlled by the bot""")
    chat_type = _(
        """Optional. Type of the chat from which the inline query was sent. Can be either “sender” for a
        private chat with the inline query sender, “private”, “group”, “supergroup”, or
        “channel”. The chat type should be always known for requests sent from official
        clients and most third-party clients, unless the request was sent from a secret chat"""
    )
    location = _(
        """Optional. Sender location, only for bots that request user location"""
    )


class InlineQueryResultArticleHelpText:
    type = _("""Type of the result, must be article""")
    telegram_id = _("""Unique identifier for this result, 1-64 Bytes""")
    title = _("""Title of the result""")
    input_message_content = _("""Content of the message to be sent""")
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    url = _("""Optional. URL of the result""")
    hide_url = _(
        """Optional. Pass True if you don't want the URL to be shown in the message"""
    )
    description = _("""Optional. Short description of the result""")
    thumb_url = _("""Optional. Url of the thumbnail for the result""")
    thumb_width = _("""Optional. Thumbnail width""")
    thumb_height = _("""Optional. Thumbnail height""")


class InlineQueryResultAudioHelpText:
    type = _("""Type of the result, must be audio""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    audio_url = _("""A valid URL for the audio file""")
    title = _("""Title""")
    caption = _("""Optional. Caption, 0-1024 characters after entities parsing""")
    parse_mode = _(
        """Optional. Mode for parsing entities in the audio caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    performer = _("""Optional. Performer""")
    audio_duration = _("""Optional. Audio duration in seconds""")
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the audio"""
    )


class InlineQueryResultCachedAudioHelpText:
    type = _("""Type of the result, must be audio""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    audio_file_id = _("""A valid file identifier for the audio file""")
    caption = _("""Optional. Caption, 0-1024 characters after entities parsing""")
    parse_mode = _(
        """Optional. Mode for parsing entities in the audio caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the audio"""
    )


class InlineQueryResultCachedDocumentHelpText:
    type = _("""Type of the result, must be document""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    title = _("""Title for the result""")
    document_file_id = _("""A valid file identifier for the file""")
    description = _("""Optional. Short description of the result""")
    caption = _(
        """Optional. Caption of the document to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the document caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the file"""
    )


class InlineQueryResultCachedGifHelpText:
    type = _("""Type of the result, must be gif""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    gif_file_id = _("""A valid file identifier for the GIF file""")
    title = _("""Optional. Title for the result""")
    caption = _(
        """Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the caption. See formatting options for more details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the GIF animation"""
    )


class InlineQueryResultCachedMpeg4GifHelpText:
    type = _("""Type of the result, must be mpeg4_gif""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    mpeg4_file_id = _("""A valid file identifier for the MPEG4 file""")
    title = _("""Optional. Title for the result""")
    caption = _(
        """Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the caption. See formatting options for more details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the video animation"""
    )


class InlineQueryResultCachedPhotoHelpText:
    type = _("""Type of the result, must be photo""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    photo_file_id = _("""A valid file identifier of the photo""")
    title = _("""Optional. Title for the result""")
    description = _("""Optional. Short description of the result""")
    caption = _(
        """Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the photo caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the photo"""
    )


class InlineQueryResultCachedStickerHelpText:
    type = _("""Type of the result, must be sticker""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    sticker_file_id = _("""A valid file identifier of the sticker""")
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the sticker"""
    )


class InlineQueryResultCachedVideoHelpText:
    type = _("""Type of the result, must be video""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    video_file_id = _("""A valid file identifier for the video file""")
    title = _("""Title for the result""")
    description = _("""Optional. Short description of the result""")
    caption = _(
        """Optional. Caption of the video to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the video caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the video"""
    )


class InlineQueryResultCachedVoiceHelpText:
    type = _("""Type of the result, must be voice""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    voice_file_id = _("""A valid file identifier for the voice message""")
    title = _("""Voice message title""")
    caption = _("""Optional. Caption, 0-1024 characters after entities parsing""")
    parse_mode = _(
        """Optional. Mode for parsing entities in the voice message caption. See formatting options for
        more details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the voice message"""
    )


class InlineQueryResultContactHelpText:
    type = _("""Type of the result, must be contact""")
    telegram_id = _("""Unique identifier for this result, 1-64 Bytes""")
    phone_number = _("""Contact's phone number""")
    first_name = _("""Contact's first name""")
    last_name = _("""Optional. Contact's last name""")
    vcard = _(
        """Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the contact"""
    )
    thumb_url = _("""Optional. Url of the thumbnail for the result""")
    thumb_width = _("""Optional. Thumbnail width""")
    thumb_height = _("""Optional. Thumbnail height""")


class InlineQueryResultDocumentHelpText:
    type = _("""Type of the result, must be document""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    title = _("""Title for the result""")
    caption = _(
        """Optional. Caption of the document to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the document caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    document_url = _("""A valid URL for the file""")
    mime_type = _(
        """MIME type of the content of the file, either “application/pdf” or “application/zip”"""
    )
    description = _("""Optional. Short description of the result""")
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the file"""
    )
    thumb_url = _("""Optional. URL of the thumbnail (JPEG only) for the file""")
    thumb_width = _("""Optional. Thumbnail width""")
    thumb_height = _("""Optional. Thumbnail height""")


class InlineQueryResultGameHelpText:
    type = _("""Type of the result, must be game""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    game_short_name = _("""Short name of the game""")
    reply_markup = _("""Optional. Inline keyboard attached to the message""")


class InlineQueryResultGifHelpText:
    type = _("""Type of the result, must be gif""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    gif_url = _("""A valid URL for the GIF file. File size must not exceed 1MB""")
    gif_width = _("""Optional. Width of the GIF""")
    gif_height = _("""Optional. Height of the GIF""")
    gif_duration = _("""Optional. Duration of the GIF in seconds""")
    thumb_url = _(
        """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result"""
    )
    thumb_mime_type = _(
        """Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or
        “video/mp4”. Defaults to “image/jpeg”"""
    )
    title = _("""Optional. Title for the result""")
    caption = _(
        """Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the caption. See formatting options for more details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the GIF animation"""
    )


class InlineQueryResultLocationHelpText:
    type = _("""Type of the result, must be location""")
    telegram_id = _("""Unique identifier for this result, 1-64 Bytes""")
    latitude = _("""Location latitude in degrees""")
    longitude = _("""Location longitude in degrees""")
    title = _("""Location title""")
    horizontal_accuracy = _(
        """Optional. The radius of uncertainty for the location, measured in meters; 0-1500"""
    )
    live_period = _(
        """Optional. Period in seconds for which the location can be updated, should be between 60 and
        86400."""
    )
    heading = _(
        """Optional. For live locations, a direction in which the user is moving, in degrees. Must be
        between 1 and 360 if specified."""
    )
    proximity_alert_radius = _(
        """Optional. For live locations, a maximum distance for proximity alerts about
        approaching another chat member, in meters. Must be between 1 and 100000
        if specified."""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the location"""
    )
    thumb_url = _("""Optional. Url of the thumbnail for the result""")
    thumb_width = _("""Optional. Thumbnail width""")
    thumb_height = _("""Optional. Thumbnail height""")


class InlineQueryResultMpeg4GifHelpText:
    type = _("""Type of the result, must be mpeg4_gif""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    mpeg4_url = _("""A valid URL for the MPEG4 file. File size must not exceed 1MB""")
    mpeg4_width = _("""Optional. Video width""")
    mpeg4_height = _("""Optional. Video height""")
    mpeg4_duration = _("""Optional. Video duration in seconds""")
    thumb_url = _(
        """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result"""
    )
    thumb_mime_type = _(
        """Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or
        “video/mp4”. Defaults to “image/jpeg”"""
    )
    title = _("""Optional. Title for the result""")
    caption = _(
        """Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the caption. See formatting options for more details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the video animation"""
    )


class InlineQueryResultPhotoHelpText:
    type = _("""Type of the result, must be photo""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    photo_url = _(
        """A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB"""
    )
    thumb_url = _("""URL of the thumbnail for the photo""")
    photo_width = _("""Optional. Width of the photo""")
    photo_height = _("""Optional. Height of the photo""")
    title = _("""Optional. Title for the result""")
    description = _("""Optional. Short description of the result""")
    caption = _(
        """Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the photo caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the photo"""
    )


class InlineQueryResultVenueHelpText:
    type = _("""Type of the result, must be venue""")
    telegram_id = _("""Unique identifier for this result, 1-64 Bytes""")
    latitude = _("""Latitude of the venue location in degrees""")
    longitude = _("""Longitude of the venue location in degrees""")
    title = _("""Title of the venue""")
    address = _("""Address of the venue""")
    foursquare_id = _("""Optional. Foursquare identifier of the venue if known""")
    foursquare_type = _(
        """Optional. Foursquare type of the venue, if known. (For example,
        “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)"""
    )
    google_place_id = _("""Optional. Google Places identifier of the venue""")
    google_place_type = _(
        """Optional. Google Places type of the venue. (See supported types.)"""
    )
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the venue"""
    )
    thumb_url = _("""Optional. Url of the thumbnail for the result""")
    thumb_width = _("""Optional. Thumbnail width""")
    thumb_height = _("""Optional. Thumbnail height""")


class InlineQueryResultVideoHelpText:
    type = _("""Type of the result, must be video""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    video_url = _("""A valid URL for the embedded video player or video file""")
    mime_type = _(
        """MIME type of the content of the video URL, “text/html” or “video/mp4”"""
    )
    thumb_url = _("""URL of the thumbnail (JPEG only) for the video""")
    title = _("""Title for the result""")
    caption = _(
        """Optional. Caption of the video to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the video caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    video_width = _("""Optional. Video width""")
    video_height = _("""Optional. Video height""")
    video_duration = _("""Optional. Video duration in seconds""")
    description = _("""Optional. Short description of the result""")
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the video. This field is
        required if InlineQueryResultVideo is used to send an HTML-page as a
        result (e.g., a YouTube video)."""
    )


class InlineQueryResultVoiceHelpText:
    type = _("""Type of the result, must be voice""")
    telegram_id = _("""Unique identifier for this result, 1-64 bytes""")
    voice_url = _("""A valid URL for the voice recording""")
    title = _("""Recording title""")
    caption = _("""Optional. Caption, 0-1024 characters after entities parsing""")
    parse_mode = _(
        """Optional. Mode for parsing entities in the voice message caption. See formatting options for
        more details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    voice_duration = _("""Optional. Recording duration in seconds""")
    reply_markup = _("""Optional. Inline keyboard attached to the message""")
    input_message_content = _(
        """Optional. Content of the message to be sent instead of the voice recording"""
    )


class InputContactMessageContentHelpText:
    phone_number = _("""Contact's phone number""")
    first_name = _("""Contact's first name""")
    last_name = _("""Optional. Contact's last name""")
    vcard = _(
        """Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes"""
    )


class InputInvoiceMessageContentHelpText:
    title = _("""Product name, 1-32 characters""")
    description = _("""Product description, 1-255 characters""")
    payload = _(
        """Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your
        internal processes."""
    )
    provider_token = _("""Payment provider token, obtained via @BotFather""")
    currency = _("""Three-letter ISO 4217 currency code, see more on currencies""")
    prices = _(
        """Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount,
        delivery cost, delivery tax, bonus, etc.)"""
    )
    max_tip_amount = _(
        """Optional. The maximum accepted amount for tips in the smallest units of the currency
        (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass
        max_tip_amount = 145. See the exp parameter in currencies.json, it shows the
        number of digits past the decimal point for each currency (2 for the majority of
        currencies). Defaults to 0"""
    )
    suggested_tip_amounts = _(
        """Optional. A JSON-serialized array of suggested amounts of tip in the smallest
        units of the currency (integer, not float/double). At most 4 suggested tip
        amounts can be specified. The suggested tip amounts must be positive,
        passed in a strictly increased order and must not exceed max_tip_amount."""
    )
    provider_data = _(
        """Optional. A JSON-serialized object for data about the invoice, which will be shared with
        the payment provider. A detailed description of the required fields should be
        provided by the payment provider."""
    )
    photo_url = _(
        """Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing
        image for a service."""
    )
    photo_size = _("""Optional. Photo size in bytes""")
    photo_width = _("""Optional. Photo width""")
    photo_height = _("""Optional. Photo height""")
    need_name = _(
        """Optional. Pass True if you require the user's full name to complete the order"""
    )
    need_phone_number = _(
        """Optional. Pass True if you require the user's phone number to complete the order"""
    )
    need_email = _(
        """Optional. Pass True if you require the user's email address to complete the order"""
    )
    need_shipping_address = _(
        """Optional. Pass True if you require the user's shipping address to complete the
        order"""
    )
    send_phone_number_to_provider = _(
        """Optional. Pass True if the user's phone number should be sent to provider"""
    )
    send_email_to_provider = _(
        """Optional. Pass True if the user's email address should be sent to provider"""
    )
    is_flexible = _(
        """Optional. Pass True if the final price depends on the shipping method"""
    )


class InputLocationMessageContentHelpText:
    latitude = _("""Latitude of the location in degrees""")
    longitude = _("""Longitude of the location in degrees""")
    horizontal_accuracy = _(
        """Optional. The radius of uncertainty for the location, measured in meters; 0-1500"""
    )
    live_period = _(
        """Optional. Period in seconds for which the location can be updated, should be between 60 and
        86400."""
    )
    heading = _(
        """Optional. For live locations, a direction in which the user is moving, in degrees. Must be
        between 1 and 360 if specified."""
    )
    proximity_alert_radius = _(
        """Optional. For live locations, a maximum distance for proximity alerts about
        approaching another chat member, in meters. Must be between 1 and 100000
        if specified."""
    )


class InputMediaAnimationHelpText:
    type = _("""Type of the result, must be animation""")
    media = _(
        """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended),
        pass an HTTP URL for Telegram to get a file from the Internet, or pass
        “attach://<file_attach_name>” to upload a new one using multipart/form-data under
        <file_attach_name> name. More information on Sending Files »"""
    )
    thumb = _(
        """Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
        supported server-side. The thumbnail should be in JPEG format and less than 200 kB in
        size. A thumbnail's width and height should not exceed 320. Ignored if the file is not
        uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as
        a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded
        using multipart/form-data under <file_attach_name>. More information on Sending Files »"""
    )
    caption = _(
        """Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the animation caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    width = _("""Optional. Animation width""")
    height = _("""Optional. Animation height""")
    duration = _("""Optional. Animation duration in seconds""")


class InputMediaAudioHelpText:
    type = _("""Type of the result, must be audio""")
    media = _(
        """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended),
        pass an HTTP URL for Telegram to get a file from the Internet, or pass
        “attach://<file_attach_name>” to upload a new one using multipart/form-data under
        <file_attach_name> name. More information on Sending Files »"""
    )
    thumb = _(
        """Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
        supported server-side. The thumbnail should be in JPEG format and less than 200 kB in
        size. A thumbnail's width and height should not exceed 320. Ignored if the file is not
        uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as
        a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded
        using multipart/form-data under <file_attach_name>. More information on Sending Files »"""
    )
    caption = _(
        """Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the audio caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    duration = _("""Optional. Duration of the audio in seconds""")
    performer = _("""Optional. Performer of the audio""")
    title = _("""Optional. Title of the audio""")


class InputMediaDocumentHelpText:
    type = _("""Type of the result, must be document""")
    media = _(
        """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended),
        pass an HTTP URL for Telegram to get a file from the Internet, or pass
        “attach://<file_attach_name>” to upload a new one using multipart/form-data under
        <file_attach_name> name. More information on Sending Files »"""
    )
    thumb = _(
        """Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
        supported server-side. The thumbnail should be in JPEG format and less than 200 kB in
        size. A thumbnail's width and height should not exceed 320. Ignored if the file is not
        uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as
        a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded
        using multipart/form-data under <file_attach_name>. More information on Sending Files »"""
    )
    caption = _(
        """Optional. Caption of the document to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the document caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    disable_content_type_detection = _(
        """Optional. Disables automatic server-side content type detection for files
        uploaded using multipart/form-data. Always True, if the document
        is sent as part of an album."""
    )


class InputMediaPhotoHelpText:
    type = _("""Type of the result, must be photo""")
    media = _(
        """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended),
        pass an HTTP URL for Telegram to get a file from the Internet, or pass
        “attach://<file_attach_name>” to upload a new one using multipart/form-data under
        <file_attach_name> name. More information on Sending Files »"""
    )
    caption = _(
        """Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the photo caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )


class InputMediaVideoHelpText:
    type = _("""Type of the result, must be video""")
    media = _(
        """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended),
        pass an HTTP URL for Telegram to get a file from the Internet, or pass
        “attach://<file_attach_name>” to upload a new one using multipart/form-data under
        <file_attach_name> name. More information on Sending Files »"""
    )
    thumb = _(
        """Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
        supported server-side. The thumbnail should be in JPEG format and less than 200 kB in
        size. A thumbnail's width and height should not exceed 320. Ignored if the file is not
        uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as
        a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded
        using multipart/form-data under <file_attach_name>. More information on Sending Files »"""
    )
    caption = _(
        """Optional. Caption of the video to be sent, 0-1024 characters after entities parsing"""
    )
    parse_mode = _(
        """Optional. Mode for parsing entities in the video caption. See formatting options for more
        details."""
    )
    caption_entities = _(
        """Optional. List of special entities that appear in the caption, which can be specified
        instead of parse_mode"""
    )
    width = _("""Optional. Video width""")
    height = _("""Optional. Video height""")
    duration = _("""Optional. Video duration in seconds""")
    supports_streaming = _(
        """Optional. Pass True if the uploaded video is suitable for streaming"""
    )


class InputTextMessageContentHelpText:
    message_text = _("""Text of the message to be sent, 1-4096 characters""")
    parse_mode = _(
        """Optional. Mode for parsing entities in the message text. See formatting options for more
        details."""
    )
    entities = _(
        """Optional. List of special entities that appear in message text, which can be specified instead
        of parse_mode"""
    )
    disable_web_page_preview = _(
        """Optional. Disables link previews for links in the sent message"""
    )


class InputVenueMessageContentHelpText:
    latitude = _("""Latitude of the venue in degrees""")
    longitude = _("""Longitude of the venue in degrees""")
    title = _("""Name of the venue""")
    address = _("""Address of the venue""")
    foursquare_id = _("""Optional. Foursquare identifier of the venue, if known""")
    foursquare_type = _(
        """Optional. Foursquare type of the venue, if known. (For example,
        “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)"""
    )
    google_place_id = _("""Optional. Google Places identifier of the venue""")
    google_place_type = _(
        """Optional. Google Places type of the venue. (See supported types.)"""
    )


class InvoiceHelpText:
    title = _("""Product name""")
    description = _("""Product description""")
    start_parameter = _(
        """Unique bot deep-linking parameter that can be used to generate this invoice"""
    )
    currency = _("""Three-letter ISO 4217 currency code""")
    total_amount = _(
        """Total price in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in
        currencies.json, it shows the number of digits past the decimal point for each
        currency (2 for the majority of currencies)."""
    )


class KeyboardButtonHelpText:
    text = _(
        """Text of the button. If none of the optional fields are used, it will be sent as a message when the
        button is pressed"""
    )
    request_contact = _(
        """Optional. If True, the user's phone number will be sent as a contact when the button is
        pressed. Available in private chats only."""
    )
    request_location = _(
        """Optional. If True, the user's current location will be sent when the button is pressed.
        Available in private chats only."""
    )
    request_poll = _(
        """Optional. If specified, the user will be asked to create a poll and send it to the bot when
        the button is pressed. Available in private chats only."""
    )
    web_app = _(
        """Optional. If specified, the described Web App will be launched when the button is pressed. The
        Web App will be able to send a “web_app_data” service message. Available in private
        chats only."""
    )


class KeyboardButtonPollTypeHelpText:
    type = _(
        """Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If
        regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed
        to create a poll of any type."""
    )


class LabeledPriceHelpText:
    label = _("""Portion label""")
    amount = _(
        """Price of the product in the smallest units of the currency (integer, not float/double). For
        example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in
        currencies.json, it shows the number of digits past the decimal point for each currency
        (2 for the majority of currencies)."""
    )


class LocationHelpText:
    longitude = _("""Longitude as defined by sender""")
    latitude = _("""Latitude as defined by sender""")
    horizontal_accuracy = _(
        """Optional. The radius of uncertainty for the location, measured in meters; 0-1500"""
    )
    live_period = _(
        """Optional. Time relative to the message sending date, during which the location can be
        updated; in seconds. For active live locations only."""
    )
    heading = _(
        """Optional. The direction in which user is moving, in degrees; 1-360. For active live locations
        only."""
    )
    proximity_alert_radius = _(
        """Optional. The maximum distance for proximity alerts about approaching another
        chat member, in meters. For sent live locations only."""
    )


class LoginUrlHelpText:
    url = _(
        """An HTTPS URL to be opened with user authorization data added to the query string when the button is
        pressed. If the user refuses to provide authorization data, the original URL without
        information about the user will be opened. The data added is the same as described in
        Receiving authorization data.NOTE: You must always check the hash of the received data to
        verify the authentication and the integrity of the data as described in Checking
        authorization."""
    )
    forward_text = _("""Optional. New text of the button in forwarded messages.""")
    bot_username = _(
        """Optional. Username of a bot, which will be used for user authorization. See Setting up a
        bot for more details. If not specified, the current bot's username will be assumed.
        The url's domain must be the same as the domain linked with the bot. See Linking
        your domain to the bot for more details."""
    )
    request_write_access = _(
        """Optional. Pass True to request the permission for your bot to send messages to the
        user."""
    )


class MaskPositionHelpText:
    point = _(
        """The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”,
        “mouth”, or “chin”."""
    )
    x_shift = _(
        """Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For
        example, choosing -1.0 will place mask just to the left of the default mask position."""
    )
    y_shift = _(
        """Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For
        example, 1.0 will place the mask just below the default mask position."""
    )
    scale = _("""Mask scaling coefficient. For example, 2.0 means double size.""")


class MenuButtonCommandsHelpText:
    type = _("""Type of the button, must be commands""")


class MenuButtonDefaultHelpText:
    type = _("""Type of the button, must be default""")


class MenuButtonWebAppHelpText:
    type = _("""Type of the button, must be web_app""")
    text = _("""Text on the button""")
    web_app = _(
        """Description of the Web App that will be launched when the user presses the button. The Web App
        will be able to send an arbitrary message on behalf of the user using the method
        answerWebAppQuery."""
    )


class MessageHelpText:
    message_id = _("""Unique message identifier inside this chat""")
    message_thread_id = _(
        """Optional. Unique identifier of a message thread to which the message belongs; for
        supergroups only"""
    )
    user = _(
        """Optional. Sender of the message; empty for messages sent to channels. For backward compatibility,
        the field contains a fake sender user in non-channel chats, if the message was sent on
        behalf of a chat."""
    )
    sender_chat = _(
        """Optional. Sender of the message, sent on behalf of a chat. For example, the channel itself
        for channel posts, the supergroup itself for messages from anonymous group
        administrators, the linked channel for messages automatically forwarded to the
        discussion group. For backward compatibility, the field from contains a fake sender
        user in non-channel chats, if the message was sent on behalf of a chat."""
    )
    date = _("""Date the message was sent in Unix time""")
    chat = _("""Conversation the message belongs to""")
    forward_from = _(
        """Optional. For forwarded messages, sender of the original message"""
    )
    forward_from_chat = _(
        """Optional. For messages forwarded from channels or from anonymous administrators,
        information about the original sender chat"""
    )
    forward_from_message_id = _(
        """Optional. For messages forwarded from channels, identifier of the original
        message in the channel"""
    )
    forward_signature = _(
        """Optional. For forwarded messages that were originally sent in channels or by an
        anonymous chat administrator, signature of the message sender if present"""
    )
    forward_sender_name = _(
        """Optional. Sender's name for messages forwarded from users who disallow adding a link
        to their account in forwarded messages"""
    )
    forward_date = _(
        """Optional. For forwarded messages, date the original message was sent in Unix time"""
    )
    is_topic_message = _("""Optional. True, if the message is sent to a forum topic""")
    is_automatic_forward = _(
        """Optional. True, if the message is a channel post that was automatically forwarded
        to the connected discussion group"""
    )
    reply_to_message = _(
        """Optional. For replies, the original message. Note that the Message object in this field
        will not contain further reply_to_message fields even if it itself is a reply."""
    )
    via_bot = _("""Optional. Bot through which the message was sent""")
    edit_date = _("""Optional. Date the message was last edited in Unix time""")
    has_protected_content = _("""Optional. True, if the message can't be forwarded""")
    media_group_id = _(
        """Optional. The unique identifier of a media message group this message belongs to"""
    )
    author_signature = _(
        """Optional. Signature of the post author for messages in channels, or the custom title of
        an anonymous group administrator"""
    )
    text = _("""Optional. For text messages, the actual UTF-8 text of the message""")
    entities = _(
        """Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that
        appear in the text"""
    )
    animation = _(
        """Optional. Message is an animation, information about the animation. For backward
        compatibility, when this field is set, the document field will also be set"""
    )
    audio = _("""Optional. Message is an audio file, information about the file""")
    document = _("""Optional. Message is a general file, information about the file""")
    photo = _("""Optional. Message is a photo, available sizes of the photo""")
    sticker = _("""Optional. Message is a sticker, information about the sticker""")
    video = _("""Optional. Message is a video, information about the video""")
    video_note = _(
        """Optional. Message is a video note, information about the video message"""
    )
    voice = _("""Optional. Message is a voice message, information about the file""")
    caption = _(
        """Optional. Caption for the animation, audio, document, photo, video or voice"""
    )
    caption_entities = _(
        """Optional. For messages with a caption, special entities like usernames, URLs, bot
        commands, etc. that appear in the caption"""
    )
    contact = _(
        """Optional. Message is a shared contact, information about the contact"""
    )
    dice = _("""Optional. Message is a dice with random value""")
    game = _(
        """Optional. Message is a game, information about the game. More about games »"""
    )
    poll = _("""Optional. Message is a native poll, information about the poll""")
    venue = _(
        """Optional. Message is a venue, information about the venue. For backward compatibility, when this
        field is set, the location field will also be set"""
    )
    location = _(
        """Optional. Message is a shared location, information about the location"""
    )
    new_chat_members = _(
        """Optional. New members that were added to the group or supergroup and information about
        them (the bot itself may be one of these members)"""
    )
    left_chat_member = _(
        """Optional. A member was removed from the group, information about them (this member may
        be the bot itself)"""
    )
    new_chat_title = _("""Optional. A chat title was changed to this value""")
    new_chat_photo = _("""Optional. A chat photo was change to this value""")
    delete_chat_photo = _("""Optional. Service message: the chat photo was deleted""")
    group_chat_created = _("""Optional. Service message: the group has been created""")
    supergroup_chat_created = _(
        """Optional. Service message: the supergroup has been created. This field can't be
        received in a message coming through updates, because bot can't be a
        member of a supergroup when it is created. It can only be found in
        reply_to_message if someone replies to a very first message in a
        directly created supergroup."""
    )
    channel_chat_created = _(
        """Optional. Service message: the channel has been created. This field can't be
        received in a message coming through updates, because bot can't be a member
        of a channel when it is created. It can only be found in reply_to_message
        if someone replies to a very first message in a channel."""
    )
    message_auto_delete_timer_changed = _(
        """Optional. Service message: auto-delete timer settings changed in the
        chat"""
    )
    migrate_to_chat_id = _(
        """Optional. The group has been migrated to a supergroup with the specified identifier.
        This number may have more than 32 significant bits and some programming
        languages may have difficulty/silent defects in interpreting it. But it has
        at most 52 significant bits, so a signed 64-bit integer or double-precision
        float type are safe for storing this identifier."""
    )
    migrate_from_chat_id = _(
        """Optional. The supergroup has been migrated from a group with the specified
        identifier. This number may have more than 32 significant bits and some
        programming languages may have difficulty/silent defects in interpreting
        it. But it has at most 52 significant bits, so a signed 64-bit integer or
        double-precision float type are safe for storing this identifier."""
    )
    pinned_message = _(
        """Optional. Specified message was pinned. Note that the Message object in this field will
        not contain further reply_to_message fields even if it is itself a reply."""
    )
    invoice = _(
        """Optional. Message is an invoice for a payment, information about the invoice. More about
        payments »"""
    )
    successful_payment = _(
        """Optional. Message is a service message about a successful payment, information about
        the payment. More about payments »"""
    )
    connected_website = _(
        """Optional. The domain name of the website on which the user has logged in. More about
        Telegram Login »"""
    )
    passport_data = _("""Optional. Telegram Passport data""")
    proximity_alert_triggered = _(
        """Optional. Service message. A user in the chat triggered another user's
        proximity alert while sharing Live Location."""
    )
    forum_topic_created = _("""Optional. Service message: forum topic created""")
    forum_topic_closed = _("""Optional. Service message: forum topic closed""")
    forum_topic_reopened = _("""Optional. Service message: forum topic reopened""")
    video_chat_scheduled = _("""Optional. Service message: video chat scheduled""")
    video_chat_started = _("""Optional. Service message: video chat started""")
    video_chat_ended = _("""Optional. Service message: video chat ended""")
    video_chat_participants_invited = _(
        """Optional. Service message: new participants invited to a video chat"""
    )
    web_app_data = _("""Optional. Service message: data sent by a Web App""")
    reply_markup = _(
        """Optional. Inline keyboard attached to the message. login_url buttons are represented as
        ordinary url buttons."""
    )


class MessageAutoDeleteTimerChangedHelpText:
    message_auto_delete_time = _(
        """New auto-delete time for messages in the chat; in seconds"""
    )


class MessageEntityHelpText:
    type = _(
        """Type of the entity. Currently, can be “mention” (@username), “hashtag” (#hashtag), “cashtag”
        ($USD), “bot_command” (/start@jobs_bot), “url” (https://telegram.org), “email” (do-not-
        reply@telegram.org), “phone_number” (+1-212-555-0123), “bold” (bold text), “italic” (italic
        text), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler”
        (spoiler message), “code” (monowidth string), “pre” (monowidth block), “text_link” (for
        clickable text URLs), “text_mention” (for users without usernames), “custom_emoji” (for
        inline custom emoji stickers)"""
    )
    offset = _("""Offset in UTF-16 code units to the start of the entity""")
    length = _("""Length of the entity in UTF-16 code units""")
    url = _(
        """Optional. For “text_link” only, URL that will be opened after user taps on the text"""
    )
    user = _("""Optional. For “text_mention” only, the mentioned user""")
    language = _(
        """Optional. For “pre” only, the programming language of the entity text"""
    )
    custom_emoji_id = _(
        """Optional. For “custom_emoji” only, unique identifier of the custom emoji. Use
        getCustomEmojiStickers to get full information about the sticker"""
    )


class MessageIdHelpText:
    message_id = _("""Unique message identifier""")


class OrderInfoHelpText:
    name = _("""Optional. User name""")
    phone_number = _("""Optional. User's phone number""")
    email = _("""Optional. User email""")
    shipping_address = _("""Optional. User shipping address""")


class PassportDataHelpText:
    data = _(
        """Array with information about documents and other Telegram Passport elements that was shared with
        the bot"""
    )
    credentials = _("""Encrypted credentials required to decrypt the data""")


class PassportElementErrorDataFieldHelpText:
    source = _("""Error source, must be data""")
    type = _(
        """The section of the user's Telegram Passport which has the error, one of “personal_details”,
        “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”"""
    )
    field_name = _("""Name of the data field which has the error""")
    data_hash = _("""Base64-encoded data hash""")
    message = _("""Error message""")


class PassportElementErrorFileHelpText:
    source = _("""Error source, must be file""")
    type = _(
        """The section of the user's Telegram Passport which has the issue, one of “utility_bill”,
        “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”"""
    )
    file_hash = _("""Base64-encoded file hash""")
    message = _("""Error message""")


class PassportElementErrorFilesHelpText:
    source = _("""Error source, must be files""")
    type = _(
        """The section of the user's Telegram Passport which has the issue, one of “utility_bill”,
        “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”"""
    )
    file_hashes = _("""List of base64-encoded file hashes""")
    message = _("""Error message""")


class PassportElementErrorFrontSideHelpText:
    source = _("""Error source, must be front_side""")
    type = _(
        """The section of the user's Telegram Passport which has the issue, one of “passport”,
        “driver_license”, “identity_card”, “internal_passport”"""
    )
    file_hash = _(
        """Base64-encoded hash of the file with the front side of the document"""
    )
    message = _("""Error message""")


class PassportElementErrorReverseSideHelpText:
    source = _("""Error source, must be reverse_side""")
    type = _(
        """The section of the user's Telegram Passport which has the issue, one of “driver_license”,
        “identity_card”"""
    )
    file_hash = _(
        """Base64-encoded hash of the file with the reverse side of the document"""
    )
    message = _("""Error message""")


class PassportElementErrorSelfieHelpText:
    source = _("""Error source, must be selfie""")
    type = _(
        """The section of the user's Telegram Passport which has the issue, one of “passport”,
        “driver_license”, “identity_card”, “internal_passport”"""
    )
    file_hash = _("""Base64-encoded hash of the file with the selfie""")
    message = _("""Error message""")


class PassportElementErrorTranslationFileHelpText:
    source = _("""Error source, must be translation_file""")
    type = _(
        """Type of element of the user's Telegram Passport which has the issue, one of “passport”,
        “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”,
        “rental_agreement”, “passport_registration”, “temporary_registration”"""
    )
    file_hash = _("""Base64-encoded file hash""")
    message = _("""Error message""")


class PassportElementErrorTranslationFilesHelpText:
    source = _("""Error source, must be translation_files""")
    type = _(
        """Type of element of the user's Telegram Passport which has the issue, one of “passport”,
        “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”,
        “rental_agreement”, “passport_registration”, “temporary_registration”"""
    )
    file_hashes = _("""List of base64-encoded file hashes""")
    message = _("""Error message""")


class PassportElementErrorUnspecifiedHelpText:
    source = _("""Error source, must be unspecified""")
    type = _("""Type of element of the user's Telegram Passport which has the issue""")
    element_hash = _("""Base64-encoded element hash""")
    message = _("""Error message""")


class PassportFileHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    file_size = _("""File size in bytes""")
    file_date = _("""Unix time when the file was uploaded""")


class PhotoSizeHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    width = _("""Photo width""")
    height = _("""Photo height""")
    file_size = _("""Optional. File size in bytes""")


class PollHelpText:
    telegram_id = _("""Unique poll identifier""")
    question = _("""Poll question, 1-300 characters""")
    options = _("""List of poll options""")
    total_voter_count = _("""Total number of users that voted in the poll""")
    is_closed = _("""True, if the poll is closed""")
    is_anonymous = _("""True, if the poll is anonymous""")
    type = _("""Poll type, currently can be “regular” or “quiz”""")
    allows_multiple_answers = _("""True, if the poll allows multiple answers""")
    correct_option_id = _(
        """Optional. 0-based identifier of the correct answer option. Available only for polls in
        the quiz mode, which are closed, or was sent (not forwarded) by the bot or to
        the private chat with the bot."""
    )
    explanation = _(
        """Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp
        icon in a quiz-style poll, 0-200 characters"""
    )
    explanation_entities = _(
        """Optional. Special entities like usernames, URLs, bot commands, etc. that appear in
        the explanation"""
    )
    open_period = _(
        """Optional. Amount of time in seconds the poll will be active after creation"""
    )
    close_date = _(
        """Optional. Point in time (Unix timestamp) when the poll will be automatically closed"""
    )


class PollAnswerHelpText:
    poll_id = _("""Unique poll identifier""")
    user = _("""The user, who changed the answer to the poll""")
    option_ids = _(
        """0-based identifiers of answer options, chosen by the user. May be empty if the user retracted
        their vote."""
    )


class PollOptionHelpText:
    text = _("""Option text, 1-100 characters""")
    voter_count = _("""Number of users that voted for this option""")


class PreCheckoutQueryHelpText:
    telegram_id = _("""Unique query identifier""")
    user = _("""User who sent the query""")
    currency = _("""Three-letter ISO 4217 currency code""")
    total_amount = _(
        """Total price in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in
        currencies.json, it shows the number of digits past the decimal point for each
        currency (2 for the majority of currencies)."""
    )
    invoice_payload = _("""Bot specified invoice payload""")
    shipping_option_id = _(
        """Optional. Identifier of the shipping option chosen by the user"""
    )
    order_info = _("""Optional. Order information provided by the user""")


class ProximityAlertTriggeredHelpText:
    traveler = _("""User that triggered the alert""")
    watcher = _("""User that set the alert""")
    distance = _("""The distance between the users""")


class ReplyKeyboardMarkupHelpText:
    keyboard = _(
        """Array of button rows, each represented by an Array of KeyboardButton objects"""
    )
    resize_keyboard = _(
        """Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make
        the keyboard smaller if there are just two rows of buttons). Defaults to false,
        in which case the custom keyboard is always of the same height as the app's
        standard keyboard."""
    )
    one_time_keyboard = _(
        """Optional. Requests clients to hide the keyboard as soon as it's been used. The
        keyboard will still be available, but clients will automatically display the
        usual letter-keyboard in the chat - the user can press a special button in the
        input field to see the custom keyboard again. Defaults to false."""
    )
    input_field_placeholder = _(
        """Optional. The placeholder to be shown in the input field when the keyboard is
        active; 1-64 characters"""
    )
    selective = _(
        """Optional. Use this parameter if you want to show the keyboard to specific users only. Targets:
        1) users that are @mentioned in the text of the Message object; 2) if the bot's
        message is a reply (has reply_to_message_id), sender of the original message.Example:
        A user requests to change the bot's language, bot replies to the request with a
        keyboard to select the new language. Other users in the group don't see the keyboard."""
    )


class ReplyKeyboardRemoveHelpText:
    remove_keyboard = _(
        """Requests clients to remove the custom keyboard (user will not be able to summon this
        keyboard; if you want to hide the keyboard from sight but keep it accessible,
        use one_time_keyboard in ReplyKeyboardMarkup)"""
    )
    selective = _(
        """Optional. Use this parameter if you want to remove the keyboard for specific users only.
        Targets: 1) users that are @mentioned in the text of the Message object; 2) if the
        bot's message is a reply (has reply_to_message_id), sender of the original
        message.Example: A user votes in a poll, bot returns confirmation message in reply to
        the vote and removes the keyboard for that user, while still showing the keyboard with
        poll options to users who haven't voted yet."""
    )


class ResponseParametersHelpText:
    migrate_to_chat_id = _(
        """Optional. The group has been migrated to a supergroup with the specified identifier.
        This number may have more than 32 significant bits and some programming
        languages may have difficulty/silent defects in interpreting it. But it has
        at most 52 significant bits, so a signed 64-bit integer or double-precision
        float type are safe for storing this identifier."""
    )
    retry_after = _(
        """Optional. In case of exceeding flood control, the number of seconds left to wait before the
        request can be repeated"""
    )


class SentWebAppMessageHelpText:
    inline_message_id = _(
        """Optional. Identifier of the sent inline message. Available only if there is an inline
        keyboard attached to the message."""
    )


class ShippingAddressHelpText:
    country_code = _("""Two-letter ISO 3166-1 alpha-2 country code""")
    state = _("""State, if applicable""")
    city = _("""City""")
    street_line1 = _("""First line for the address""")
    street_line2 = _("""Second line for the address""")
    post_code = _("""Address post code""")


class ShippingOptionHelpText:
    telegram_id = _("""Shipping option identifier""")
    title = _("""Option title""")
    prices = _("""List of price portions""")


class ShippingQueryHelpText:
    telegram_id = _("""Unique query identifier""")
    user = _("""User who sent the query""")
    invoice_payload = _("""Bot specified invoice payload""")
    shipping_address = _("""User specified shipping address""")


class StickerHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    type = _(
        """Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is
        independent from its format, which is determined by the fields is_animated and is_video."""
    )
    width = _("""Sticker width""")
    height = _("""Sticker height""")
    is_animated = _("""True, if the sticker is animated""")
    is_video = _("""True, if the sticker is a video sticker""")
    thumb = _("""Optional. Sticker thumbnail in the .WEBP or .JPG format""")
    emoji = _("""Optional. Emoji associated with the sticker""")
    set_name = _("""Optional. Name of the sticker set to which the sticker belongs""")
    premium_animation = _(
        """Optional. For premium regular stickers, premium animation for the sticker"""
    )
    mask_position = _(
        """Optional. For mask stickers, the position where the mask should be placed"""
    )
    custom_emoji_id = _(
        """Optional. For custom emoji stickers, unique identifier of the custom emoji"""
    )
    file_size = _("""Optional. File size in bytes""")


class StickerSetHelpText:
    name = _("""Sticker set name""")
    title = _("""Sticker set title""")
    sticker_type = _(
        """Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”"""
    )
    is_animated = _("""True, if the sticker set contains animated stickers""")
    is_video = _("""True, if the sticker set contains video stickers""")
    stickers = _("""List of all set stickers""")
    thumb = _("""Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format""")


class SuccessfulPaymentHelpText:
    currency = _("""Three-letter ISO 4217 currency code""")
    total_amount = _(
        """Total price in the smallest units of the currency (integer, not float/double). For example,
        for a price of US$ 1.45 pass amount = 145. See the exp parameter in
        currencies.json, it shows the number of digits past the decimal point for each
        currency (2 for the majority of currencies)."""
    )
    invoice_payload = _("""Bot specified invoice payload""")
    shipping_option_id = _(
        """Optional. Identifier of the shipping option chosen by the user"""
    )
    order_info = _("""Optional. Order information provided by the user""")
    telegram_payment_charge_id = _("""Telegram payment identifier""")
    provider_payment_charge_id = _("""Provider payment identifier""")


class UpdateHelpText:
    update_id = _(
        """The update's unique identifier. Update identifiers start from a certain positive number and
        increase sequentially. This ID becomes especially handy if you're using webhooks,
        since it allows you to ignore repeated updates or to restore the correct update
        sequence, should they get out of order. If there are no new updates for at least a
        week, then identifier of the next update will be chosen randomly instead of
        sequentially."""
    )
    message = _(
        """Optional. New incoming message of any kind - text, photo, sticker, etc."""
    )
    edited_message = _(
        """Optional. New version of a message that is known to the bot and was edited"""
    )
    channel_post = _(
        """Optional. New incoming channel post of any kind - text, photo, sticker, etc."""
    )
    edited_channel_post = _(
        """Optional. New version of a channel post that is known to the bot and was edited"""
    )
    inline_query = _("""Optional. New incoming inline query""")
    chosen_inline_result = _(
        """Optional. The result of an inline query that was chosen by a user and sent to their
        chat partner. Please see our documentation on the feedback collecting for
        details on how to enable these updates for your bot."""
    )
    callback_query = _("""Optional. New incoming callback query""")
    shipping_query = _(
        """Optional. New incoming shipping query. Only for invoices with flexible price"""
    )
    pre_checkout_query = _(
        """Optional. New incoming pre-checkout query. Contains full information about checkout"""
    )
    poll = _(
        """Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent
        by the bot"""
    )
    poll_answer = _(
        """Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only
        in polls that were sent by the bot itself."""
    )
    my_chat_member = _(
        """Optional. The bot's chat member status was updated in a chat. For private chats, this
        update is received only when the bot is blocked or unblocked by the user."""
    )
    chat_member = _(
        """Optional. A chat member's status was updated in a chat. The bot must be an administrator in
        the chat and must explicitly specify “chat_member” in the list of allowed_updates to
        receive these updates."""
    )
    chat_join_request = _(
        """Optional. A request to join the chat has been sent. The bot must have the
        can_invite_users administrator right in the chat to receive these updates."""
    )


class UserHelpText:
    telegram_id = _(
        """Unique identifier for this user or bot. This number may have more than 32 significant bits
        and some programming languages may have difficulty/silent defects in interpreting
        it. But it has at most 52 significant bits, so a 64-bit integer or double-precision
        float type are safe for storing this identifier."""
    )
    is_bot = _("""True, if this user is a bot""")
    first_name = _("""User's or bot's first name""")
    last_name = _("""Optional. User's or bot's last name""")
    username = _("""Optional. User's or bot's username""")
    language_code = _("""Optional. IETF language tag of the user's language""")
    is_premium = _("""Optional. True, if this user is a Telegram Premium user""")
    added_to_attachment_menu = _(
        """Optional. True, if this user added the bot to the attachment menu"""
    )
    can_join_groups = _(
        """Optional. True, if the bot can be invited to groups. Returned only in getMe."""
    )
    can_read_all_group_messages = _(
        """Optional. True, if privacy mode is disabled for the bot. Returned only in
        getMe."""
    )
    supports_inline_queries = _(
        """Optional. True, if the bot supports inline queries. Returned only in getMe."""
    )


class UserProfilePhotosHelpText:
    total_count = _("""Total number of profile pictures the target user has""")
    photos = _("""Requested profile pictures (in up to 4 sizes each)""")


class VenueHelpText:
    location = _("""Venue location. Can't be a live location""")
    title = _("""Name of the venue""")
    address = _("""Address of the venue""")
    foursquare_id = _("""Optional. Foursquare identifier of the venue""")
    foursquare_type = _(
        """Optional. Foursquare type of the venue. (For example, “arts_entertainment/default”,
        “arts_entertainment/aquarium” or “food/icecream”.)"""
    )
    google_place_id = _("""Optional. Google Places identifier of the venue""")
    google_place_type = _(
        """Optional. Google Places type of the venue. (See supported types.)"""
    )


class VideoHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    width = _("""Video width as defined by sender""")
    height = _("""Video height as defined by sender""")
    duration = _("""Duration of the video in seconds as defined by sender""")
    thumb = _("""Optional. Video thumbnail""")
    file_name = _("""Optional. Original filename as defined by sender""")
    mime_type = _("""Optional. MIME type of the file as defined by sender""")
    file_size = _(
        """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may
        have difficulty/silent defects in interpreting it. But it has at most 52 significant
        bits, so a signed 64-bit integer or double-precision float type are safe for storing
        this value."""
    )


class VideoChatEndedHelpText:
    duration = _("""Video chat duration in seconds""")


class VideoChatParticipantsInvitedHelpText:
    users = _("""New members that were invited to the video chat""")


class VideoChatScheduledHelpText:
    start_date = _(
        """Point in time (Unix timestamp) when the video chat is supposed to be started by a chat
        administrator"""
    )


class VideoNoteHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    length = _(
        """Video width and height (diameter of the video message) as defined by sender"""
    )
    duration = _("""Duration of the video in seconds as defined by sender""")
    thumb = _("""Optional. Video thumbnail""")
    file_size = _("""Optional. File size in bytes""")


class VoiceHelpText:
    file_id = _(
        """Identifier for this file, which can be used to download or reuse the file"""
    )
    file_unique_id = _(
        """Unique identifier for this file, which is supposed to be the same over time and for
        different bots. Can't be used to download or reuse the file."""
    )
    duration = _("""Duration of the audio in seconds as defined by sender""")
    mime_type = _("""Optional. MIME type of the file as defined by sender""")
    file_size = _(
        """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may
        have difficulty/silent defects in interpreting it. But it has at most 52 significant
        bits, so a signed 64-bit integer or double-precision float type are safe for storing
        this value."""
    )


class WebAppDataHelpText:
    data = _(
        """The data. Be aware that a bad client can send arbitrary data in this field."""
    )
    button_text = _(
        """Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad
        client can send arbitrary data in this field."""
    )


class WebAppInfoHelpText:
    url = _(
        """An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps"""
    )


class WebhookInfoHelpText:
    url = _("""Webhook URL, may be empty if webhook is not set up""")
    has_custom_certificate = _(
        """True, if a custom certificate was provided for webhook certificate checks"""
    )
    pending_update_count = _("""Number of updates awaiting delivery""")
    ip_address = _("""Optional. Currently used webhook IP address""")
    last_error_date = _(
        """Optional. Unix time for the most recent error that happened when trying to deliver an
        update via webhook"""
    )
    last_error_message = _(
        """Optional. Error message in human-readable format for the most recent error that
        happened when trying to deliver an update via webhook"""
    )
    last_synchronization_error_date = _(
        """Optional. Unix time of the most recent error that happened when trying
        to synchronize available updates with Telegram datacenters"""
    )
    max_connections = _(
        """Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook
        for update delivery"""
    )
    allowed_updates = _(
        """Optional. A list of update types the bot is subscribed to. Defaults to all update types
        except chat_member"""
    )
