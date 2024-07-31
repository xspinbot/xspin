from aiogram.filters import Filter

class Text(Filter):
    def __init__(self, text: str = None, startswith: str = None) -> None:
        self.text = text
        self.startswith = startswith

    async def __call__(self, event: object) -> bool:
        text: str = event.dict()['text']
        text = text.lower()

        return (text == self.text) if self.text else (
            text.startswith(self.startswith) if self.startswith else True)
        