from aiogram import Router, Dispatcher

from bot.misc import dp
from bot.utils.helpful_functions import router
from bot.routers import (users, groups, admins, users_commands, admin_commands, 
                     groups_commands, games, settings, commands)


async def include_routers():
    return (
        router(dispatcher = dp, router = users),
        router(dispatcher = dp, router = groups),
        router(dispatcher = dp, router = admins),
        router(dispatcher = dp, router = commands),

        router(dispatcher = users, router = users_commands),
        router(dispatcher = users, router = settings),
        router(dispatcher = groups, router = groups_commands),
        router(dispatcher = groups, router = games),
        router(dispatcher = admins, router = admin_commands)
    )