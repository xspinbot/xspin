from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.i18n import gettext
from bot.misc import bot_settings

_ = gettext

async def button(admin: bool = False):
    kb = InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(
                    text = _("➕ Добавить в группу"), 
                    url = "http://t.me/xspingamebot?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton(
                    text = _("📃 Документация"),
                    web_app = WebAppInfo(
                        url = f"{bot_settings.web_app_url}"
                    )
                )
            ]
        ]
    )

    if admin: kb.inline_keyboard.append([InlineKeyboardButton(
            text = _("🛠 Панель администратора"), 
            web_app = WebAppInfo(url = f"{bot_settings.web_app_url}/admin"))])
        
    return kb