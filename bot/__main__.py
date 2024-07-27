import asyncio

from bot.misc import dp, bot
from bot.misc import i18n as I18nMiddleware

from bot.utils import logging, include_routers
from bot.filters import Chat
from bot.middlewares.create import CreateUserAndChatMiddleware
from bot import handlers


async def main():
    I18nMiddleware.setup(dp)
    dp.message.middleware(CreateUserAndChatMiddleware())
    dp.message.filter(Chat)

    await include_routers.include_routers()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())