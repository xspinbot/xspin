from aiogram.filters import Filter
from aiogram.enums import ChatType

from aiogram.types import Chat

class Chat(Filter):
    def __init__(self, *args) -> None:
        self.chat_type = ''
    
    def is_private(self):
        self.chat_type = (ChatType.PRIVATE, )
        return self
    
    def is_channel(self):
        self.chat_type = (ChatType.CHANNEL, )
        return self
    
    def is_group(self):
        self.chat_type = (ChatType.SUPERGROUP, ChatType.GROUP, )
        return self
    
    async def __call__(self, event: object) -> bool:
        chat_type = event.dict()['chat']['type']
        return chat_type in self.chat_type