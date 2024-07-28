from aiogram import Dispatcher

from bot.middlewares.create import CreateUserAndChatMiddleware
from bot.misc import i18n as I18nMiddleware

from bot.filters.chat_type import Chat


async def setup_middlewares(dispatcher: Dispatcher):
    I18nMiddleware.setup(dispatcher)
    dispatcher.message.middleware(CreateUserAndChatMiddleware())

async def setup_filters(dispatcher: Dispatcher):
    dispatcher.message.filter(Chat)
