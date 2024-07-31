from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n

from data.config import BotSettings
from bot.middlewares.i18n import I18nMiddleware

bot_settings = BotSettings()
storage = MemoryStorage()
dp = Dispatcher(
    storage = storage
)
bot = Bot(
    token = bot_settings.token,
    default = DefaultBotProperties(
        parse_mode = ParseMode.HTML
    )
)
i18n: I18nMiddleware = I18nMiddleware(
    i18n = I18n(
        path = 'bot/locales',
        domain = 'messages',
        default_locale = 'ru'
    )
)