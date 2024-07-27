import asyncio
from bot.misc import dp, bot
from bot.utils import logging, include_routers
from bot import middlewares, handlers


async def main():
    from bot.misc import dp as dispatcher
    from bot.misc import i18n as I18nMiddleware

    I18nMiddleware.setup(dispatcher)

    await include_routers.include_routers()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())