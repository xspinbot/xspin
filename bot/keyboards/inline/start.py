from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

def button():
    return InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(
                    text = "➕ Добавить в группу", 
                    url = "http://t.me/xspingamebot?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton(
                    text = "📃 Документация",
                    web_app = WebAppInfo(
                        url = "https://7389-87-237-239-49.ngrok-free.app/games"
                    )
                )
            ],
            [
                InlineKeyboardButton(
                    text = "🛠 Панель администратора",
                    web_app = WebAppInfo(
                        url = "https://7389-87-237-239-49.ngrok-free.app/admin"
                    )
                )
            ]
        ]
    )