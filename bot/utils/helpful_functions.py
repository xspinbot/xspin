from aiogram import Dispatcher, Router

def router(dispatcher: Dispatcher, router: Router) -> Dispatcher | Router:
    return dispatcher.include_router(router = router)
