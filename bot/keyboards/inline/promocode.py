from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.i18n import gettext
from bot.misc import bot_settings

_ = gettext

async def created(promocode: str):
    return InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(
                    text = _("📨 Отправить в чат XSpinGame"), 
                    callback_data = f'send_to_chat_{promocode}'
                )
            ],
            [
                InlineKeyboardButton(
                    text=_("📤 Отправить всем пользователям и чатам"),
                    callback_data = f'send_to_all_{promocode}'
                )
            ],
            [
                InlineKeyboardButton(
                    text = _("👤 Отправить всем пользователям"),
                    callback_data = f'send_to_all_users_{promocode}'
                ),
                InlineKeyboardButton(
                    text = _("💬 Отправить во все чаты"),
                    callback_data = f'send_to_all_chat_{promocode}'
                )
            ],
            [
                InlineKeyboardButton(
                    text = _("🔗 Ссылка для активации промокода"),
                    url = f'https://t.me/{bot_settings.name}?start=promocode_{promocode}'
                )
            ]
        ]
    )

async def already_exists(promocode: str):
    return InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(
                    text = _("🔄 Удалить и создать заново"),
                    callback_data = f'delete_and_create_again_{promocode}'
                )
            ]
        ]
    )