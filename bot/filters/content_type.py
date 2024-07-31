from aiogram.filters import Filter
from aiogram.types import Message
from aiogram import enums
from bot.misc import bot

def get_content_type(data: dict):
    if data['text']:
        return enums.ContentType.TEXT
    if data['audio']:
        return enums.ContentType.AUDIO
    if data['animation']:
        return enums.ContentType.ANIMATION
    if data['document']:
        return enums.ContentType.DOCUMENT
    if data['game']:
        return enums.ContentType.GAME
    if data['photo']:
        return enums.ContentType.PHOTO
    if data['sticker']:
        return enums.ContentType.STICKER
    if data['video']:
        return enums.ContentType.VIDEO
    if data['video_note']:
        return enums.ContentType.VIDEO_NOTE
    if data['voice']:
        return enums.ContentType.VOICE
    if data['contact']:
        return enums.ContentType.CONTACT
    if data['venue']:
        return enums.ContentType.VENUE
    if data['location']:
        return enums.ContentType.LOCATION
    if data['new_chat_members']:
        return enums.ContentType.NEW_CHAT_MEMBERS
    if data['left_chat_member']:
        return enums.ContentType.LEFT_CHAT_MEMBER
    if data['invoice']:
        return enums.ContentType.INVOICE
    if data['successful_payment']:
        return enums.ContentType.SUCCESSFUL_PAYMENT
    if data['users_shared']:
        return enums.ContentType.USERS_SHARED
    if data['connected_website']:
        return enums.ContentType.CONNECTED_WEBSITE
    if data['migrate_from_chat_id']:
        return enums.ContentType.MIGRATE_FROM_CHAT_ID
    if data['migrate_to_chat_id']:
        return enums.ContentType.MIGRATE_TO_CHAT_ID
    if data['pinned_message']:
        return enums.ContentType.PINNED_MESSAGE
    if data['new_chat_title']:
        return enums.ContentType.NEW_CHAT_TITLE
    if data['new_chat_photo']:
        return enums.ContentType.NEW_CHAT_PHOTO
    if data['delete_chat_photo']:
        return enums.ContentType.DELETE_CHAT_PHOTO
    if data['group_chat_created']:
        return enums.ContentType.GROUP_CHAT_CREATED
    if data['supergroup_chat_created']:
        return enums.ContentType.SUPERGROUP_CHAT_CREATED
    if data['channel_chat_created']:
        return enums.ContentType.CHANNEL_CHAT_CREATED
    if data['paid_media']:
        return enums.ContentType.PAID_MEDIA
    if data['passport_data']:
        return enums.ContentType.PASSPORT_DATA
    if data['proximity_alert_triggered']:
        return enums.ContentType.PROXIMITY_ALERT_TRIGGERED
    if data['poll']:
        return enums.ContentType.POLL
    if data['dice']:
        return enums.ContentType.DICE
    if data['message_auto_delete_timer_changed']:
        return enums.ContentType.MESSAGE_AUTO_DELETE_TIMER_CHANGED
    if data['forum_topic_created']:
        return enums.ContentType.FORUM_TOPIC_CREATED
    if data['forum_topic_edited']:
        return enums.ContentType.FORUM_TOPIC_EDITED
    if data['forum_topic_closed']:
        return enums.ContentType.FORUM_TOPIC_CLOSED
    if data['forum_topic_reopened']:
        return enums.ContentType.FORUM_TOPIC_REOPENED
    if data['general_forum_topic_hidden']:
        return enums.ContentType.GENERAL_FORUM_TOPIC_HIDDEN
    if data['general_forum_topic_unhidden']:
        return enums.ContentType.GENERAL_FORUM_TOPIC_UNHIDDEN
    if data['giveaway_created']:
        return enums.ContentType.GIVEAWAY_CREATED
    if data['giveaway']:
        return enums.ContentType.GIVEAWAY
    if data['giveaway_completed']:
        return enums.ContentType.GIVEAWAY_COMPLETED
    if data['giveaway_winners']:
        return enums.ContentType.GIVEAWAY_WINNERS
    if data['video_chat_scheduled']:
        return enums.ContentType.VIDEO_CHAT_SCHEDULED
    if data['video_chat_started']:
        return enums.ContentType.VIDEO_CHAT_STARTED
    if data['video_chat_ended']:
        return enums.ContentType.VIDEO_CHAT_ENDED
    if data['video_chat_participants_invited']:
        return enums.ContentType.VIDEO_CHAT_PARTICIPANTS_INVITED
    if data['web_app_data']:
        return enums.ContentType.WEB_APP_DATA
    if data['user_shared']:
        return enums.ContentType.USER_SHARED
    if data['chat_shared']:
        return enums.ContentType.CHAT_SHARED
    if data['story']:
        return enums.ContentType.STORY
    if data['write_access_allowed']:
        return enums.ContentType.WRITE_ACCESS_ALLOWED
    if data['chat_background_set']:
        return enums.ContentType.CHAT_BACKGROUND_SET
    if data['boost_added']:
        return enums.ContentType.BOOST_ADDED
    if data['refunded_payment']:
        return enums.ContentType.REFUNDED_PAYMENT

    return enums.ContentType.UNKNOWN


class ContentType(Filter):
    UNKNOWN = "unknown"
    ANY = "any"
    TEXT = "text"
    ANIMATION = "animation"
    AUDIO = "audio"
    DOCUMENT = "document"
    PAID_MEDIA = "paid_media"
    PHOTO = "photo"
    STICKER = "sticker"
    STORY = "story"
    VIDEO = "video"
    VIDEO_NOTE = "video_note"
    VOICE = "voice"
    CONTACT = "contact"
    DICE = "dice"
    GAME = "game"
    POLL = "poll"
    VENUE = "venue"
    LOCATION = "location"
    NEW_CHAT_MEMBERS = "new_chat_members"
    LEFT_CHAT_MEMBER = "left_chat_member"
    NEW_CHAT_TITLE = "new_chat_title"
    NEW_CHAT_PHOTO = "new_chat_photo"
    DELETE_CHAT_PHOTO = "delete_chat_photo"
    GROUP_CHAT_CREATED = "group_chat_created"
    SUPERGROUP_CHAT_CREATED = "supergroup_chat_created"
    CHANNEL_CHAT_CREATED = "channel_chat_created"
    MESSAGE_AUTO_DELETE_TIMER_CHANGED = "message_auto_delete_timer_changed"
    MIGRATE_TO_CHAT_ID = "migrate_to_chat_id"
    MIGRATE_FROM_CHAT_ID = "migrate_from_chat_id"
    PINNED_MESSAGE = "pinned_message"
    INVOICE = "invoice"
    SUCCESSFUL_PAYMENT = "successful_payment"
    REFUNDED_PAYMENT = "refunded_payment"
    USERS_SHARED = "users_shared"
    CHAT_SHARED = "chat_shared"
    CONNECTED_WEBSITE = "connected_website"
    WRITE_ACCESS_ALLOWED = "write_access_allowed"
    PASSPORT_DATA = "passport_data"
    PROXIMITY_ALERT_TRIGGERED = "proximity_alert_triggered"
    BOOST_ADDED = "boost_added"
    CHAT_BACKGROUND_SET = "chat_background_set"
    FORUM_TOPIC_CREATED = "forum_topic_created"
    FORUM_TOPIC_EDITED = "forum_topic_edited"
    FORUM_TOPIC_CLOSED = "forum_topic_closed"
    FORUM_TOPIC_REOPENED = "forum_topic_reopened"
    GENERAL_FORUM_TOPIC_HIDDEN = "general_forum_topic_hidden"
    GENERAL_FORUM_TOPIC_UNHIDDEN = "general_forum_topic_unhidden"
    GIVEAWAY_CREATED = "giveaway_created"
    GIVEAWAY = "giveaway"
    GIVEAWAY_WINNERS = "giveaway_winners"
    GIVEAWAY_COMPLETED = "giveaway_completed"
    VIDEO_CHAT_SCHEDULED = "video_chat_scheduled"
    VIDEO_CHAT_STARTED = "video_chat_started"
    VIDEO_CHAT_ENDED = "video_chat_ended"
    VIDEO_CHAT_PARTICIPANTS_INVITED = "video_chat_participants_invited"
    WEB_APP_DATA = "web_app_data"
    USER_SHARED = "user_shared"
    
    def __init__(self, content_type = None) -> None:
        self.content_type = content_type
    
    async def __call__(self, event: object) -> bool:
        data = event.dict()

        return (get_content_type(data=data) == self.content_type) if self.content_type else True