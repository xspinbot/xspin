import time

from aiogram import Dispatcher, Router, types, html
from aiogram.enums import DiceEmoji
from aiogram.utils.i18n import gettext

from sqlalchemy.orm import Session
from db import repository as repo

_ = gettext

def router(dispatcher: Dispatcher, router: Router) -> Dispatcher | Router:
    return dispatcher.include_router(router = router)

def wait(seconds: float = 2):
    time.sleep(seconds)

class Play:
    def __init__(self) -> None:
        self.won_false = {"won": False}

        self.games = {
            DiceEmoji.BASKETBALL: 'basketball',
            DiceEmoji.FOOTBALL: 'football',
            DiceEmoji.DART: 'dart',
            DiceEmoji.BOWLING: 'bowling',
            DiceEmoji.SLOT_MACHINE: 'slot_machine'
        }

    def won_true(self, balance: int, bid: int, multiply: int):
        return {"won": True, "balance": int(balance + (bid * multiply)), "prize": int(bid * multiply)}

    def check(self, balance, bid):
        return {
            DiceEmoji.BASKETBALL: {
                1: self.won_false,
                2: self.won_false,
                3: self.won_false,
                4: self.won_true(balance, bid, 2),
                5: self.won_true(balance, bid, 3)
            },

            DiceEmoji.FOOTBALL: {
                1: self.won_false,
                2: self.won_false,
                3: self.won_false,
                4: self.won_true(balance, bid, 2),
                5: self.won_true(balance, bid, 3)
            },

            DiceEmoji.DART: {
                1: self.won_false,
                2: self.won_false,
                3: self.won_false,
                4: self.won_false,
                5: self.won_false,
                6: self.won_true(balance, bid, 4)
            },

            DiceEmoji.BOWLING: {
                1: self.won_false,
                2: self.won_false,
                3: self.won_false,
                4: self.won_false,
                5: self.won_true(balance, bid, 2),
                6: self.won_true(balance, bid, 3)
            },

            DiceEmoji.SLOT_MACHINE: {
                1: ("bar", "bar", "bar"),
                2: ("grape", "bar", "bar"),
                3: ("lemon", "bar", "bar"),
                4: ("seven", "bar", "bar"),
                5: ("bar", "grape", "bar"),
                6: ("grape", "grape", "bar"),
                7: ("lemon", "grape", "bar"),
                8: ("seven", "grape", "bar"),
                9: ("bar", "lemon", "bar"),
                10: ("grape", "lemon", "bar"),
                11: ("lemon", "lemon", "bar"),
                12: ("seven", "lemon", "bar"),
                13: ("bar", "seven", "bar"),
                14: ("grape", "seven", "bar"),
                15: ("lemon", "seven", "bar"),
                16: ("seven", "seven", "bar"),
                17: ("bar", "bar", "grape"),
                18: ("grape", "bar", "grape"),
                19: ("lemon", "bar", "grape"),
                20: ("seven", "bar", "grape"),
                21: ("bar", "grape", "grape"),
                22: ("grape", "grape", "grape"),
                23: ("lemon", "grape", "grape"),
                24: ("seven", "grape", "grape"),
                25: ("bar", "lemon", "grape"),
                26: ("grape", "lemon", "grape"),
                27: ("lemon", "lemon", "grape"),
                28: ("seven", "lemon", "grape"),
                29: ("bar", "seven", "grape"),
                30: ("grape", "seven", "grape"),
                31: ("lemon", "seven", "grape"),
                32: ("seven", "seven", "grape"),
                33: ("bar", "bar", "lemon"),
                34: ("grape", "bar", "lemon"),
                35: ("lemon", "bar", "lemon"),
                36: ("seven", "bar", "lemon"),
                37: ("bar", "grape", "lemon"),
                38: ("grape", "grape", "lemon"),
                39: ("lemon", "grape", "lemon"),
                40: ("seven", "grape", "lemon"),
                41: ("bar", "lemon", "lemon"),
                42: ("grape", "lemon", "lemon"),
                43: ("lemon", "lemon", "lemon"),
                44: ("seven", "lemon", "lemon"),
                45: ("bar", "seven", "lemon"),
                46: ("grape", "seven", "lemon"),
                47: ("lemon", "seven", "lemon"),
                48: ("seven", "seven", "lemon"),
                49: ("bar", "bar", "seven"),
                50: ("grape", "bar", "seven"),
                51: ("lemon", "bar", "seven"),
                52: ("seven", "bar", "seven"),
                53: ("bar", "grape", "seven"),
                54: ("grape", "grape", "seven"),
                55: ("lemon", "grape", "seven"),
                56: ("seven", "grape", "seven"),
                57: ("bar", "lemon", "seven"),
                58: ("grape", "lemon", "seven"),
                59: ("lemon", "lemon", "seven"),
                60: ("seven", "lemon", "seven"),
                61: ("bar", "seven", "seven"),
                62: ("grape", "seven", "seven"),
                63: ("lemon", "seven", "seven"),
                64: ("seven", "seven", "seven"),
            }
        }
    
    def check_slot_machine(self, outcome: tuple, balance: int, bid: int):
        if outcome == ("seven", "seven", "seven"):
            return self.won_true(balance, bid, 6)
        elif outcome == ("bar", "bar", "bar"):
            return self.won_true(balance, bid, 4.5)
        elif outcome.count("seven") == 2:
            if (outcome[0] == outcome[1]) or (outcome[1] == outcome[2]):
                return self.won_true(balance, bid, 2)
        elif outcome in [("lemon", "lemon", "lemon"), ("grape", "grape", "grape")]:
            return self.won_true(balance, bid, 3)
        elif outcome.count("bar") == 2:
            if (outcome[0] == outcome[1]) or (outcome[1] == outcome[2]):
                return self.won_true(balance, bid, 1.5)
        elif outcome.count("grape") == 2 or outcome.count("lemon") == 2:
            if (outcome[0] == outcome[1]) or (outcome[1] == outcome[2]):
                return self.won_true(balance, bid, 1.25)
        else:
            return self.won_false
    

    async def play(self, message: types.Message, game: str, session: Session):
        text = message.text.lower()

        if len(text.split()) == 2:
            try:
                bid = int(text.split()[1])
                balance = await repo.UsersTableRepository().get_balance(
                    user_id=message.from_user.id, session=session)
                
                if balance >= bid:
                    new_balance = balance - bid
                    await repo.UsersTableRepository().update_balance(user_id=message.from_user.id,
                        balance=new_balance, session=session)

                    dice = await message.reply_dice(emoji=game)
                    value = dice.dice.value
                    wait(2.5)

                    checking = self.check(balance - bid, bid)[game][value]
                    if game == DiceEmoji.SLOT_MACHINE:
                        checking = self.check_slot_machine(checking, balance - bid, bid)

                    await repo.GamesHistoryTableRepository().create_game(
                        user_id=message.from_user.id,
                        chat_id=message.chat.id,
                        game=self.games[game],
                        bid=bid,
                        is_won=checking['won'],
                        session=session)

                    if checking['won']:
                        await repo.UsersTableRepository().update_balance(user_id=message.from_user.id,
                            balance=checking['balance'],
                            session=session)
                        
                        await message.reply(html.bold(
                            _("🏆 Вы победили") + "\n\n" + _("Сумма выигрыша — ") + f"{checking['prize']} 💰."
                        ))
                    else:
                        await message.reply(html.bold(
                            _("Вы проиграли 😔")
                        ))
                        
                else:
                    await message.reply(html.bold(
                        _("Ваш баланс недостаточен! В балансе: ") + f"{balance} 💰"))
    
            except ValueError:
                await message.reply(html.bold(_("Введена неверная сумма ❌")))

        else:
            if len(text.split()) == 1:
                await message.reply(html.bold(_("Сумма не введена ❌")))

        
def transfer_limit(level: int = 1):
    return level * 500000

def upgrade_limit_level_price(level: int = 1):
    return level * 750000

def top_balance(balance: int):
    len_balance = len(str(balance))
    str_balance = str(balance)

    if len_balance == 7:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}M"
        return balance_result
    elif len_balance == 8:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}M"
        return balance_result
    elif len_balance == 9:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}M"
        return balance_result
    elif len_balance == 10:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}B"
        return balance_result
    elif len_balance == 11:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}B"
        return balance_result
    elif len_balance == 12:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}B"
        return balance_result
    elif len_balance == 13:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}T"
        return balance_result
    elif len_balance == 14:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}T"
        return balance_result
    elif len_balance == 6:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}K"
        return balance_result
    elif len_balance == 5:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}K"
        return balance_result
    elif len_balance == 4:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}K"
        return balance_result
    elif len_balance == 15:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}T"
        return balance_result
    elif len_balance == 16:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}q"
        return balance_result
    elif len_balance == 17:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}q"
        return balance_result
    elif len_balance == 18:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}q"
        return balance_result
    elif len_balance == 19:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}Q"
        return balance_result
    elif len_balance == 20:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}Q"
        return balance_result
    elif len_balance == 21:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}Q"
        return balance_result
    elif len_balance == 22:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}s"
        return balance_result
    elif len_balance == 23:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}s"
        return balance_result
    elif len_balance == 24:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}s"
        return balance_result
    elif len_balance == 25:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}S"
        return balance_result
    elif len_balance == 26:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}S"
        return balance_result
    elif len_balance == 27:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}S"
        return balance_result
    elif len_balance == 28:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}O"
        return balance_result
    elif len_balance == 29:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}O"
        return balance_result
    elif len_balance == 30:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}O"
        return balance_result
    elif len_balance == 31:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}N"
        return balance_result
    elif len_balance == 32:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}N"
        return balance_result
    elif len_balance == 33:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}N"
        return balance_result
    elif len_balance == 34:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}d"
        return balance_result
    elif len_balance == 35:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}d"
        return balance_result
    elif len_balance == 36:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}d"
        return balance_result
    elif len_balance == 37:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}U"
        return balance_result
    elif len_balance == 38:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}U"
        return balance_result
    elif len_balance == 39:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}U"
        return balance_result
    elif len_balance == 40:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}D"
        return balance_result
    elif len_balance == 41:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}D"
        return balance_result
    elif len_balance == 42:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}D"
        return balance_result
    elif len_balance == 43:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}Tre"
        return balance_result
    elif len_balance == 44:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}Tre"
        return balance_result
    elif len_balance == 45:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}Tre"
        return balance_result
    elif len_balance == 46:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}Qua"
        return balance_result
    elif len_balance == 47:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}Qua"
        return balance_result
    elif len_balance == 48:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}Qua"
        return balance_result
    elif len_balance == 49:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}Qui"
        return balance_result
    elif len_balance == 50:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}Qui"
        return balance_result
    elif len_balance == 51:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}Qui"
        return balance_result
    elif len_balance == 52:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}SE"
        return balance_result
    elif len_balance == 53:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}SE"
        return balance_result
    elif len_balance == 54:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}SE"
        return balance_result
    elif len_balance == 55:
        balance_numbers = str_balance[0:1]
        balance_result = f"{balance_numbers}SEP"
        return balance_result
    elif len_balance == 56:
        balance_numbers = str_balance[0:2]
        balance_result = f"{balance_numbers}SEP"
        return balance_result
    elif len_balance == 57:
        balance_numbers = str_balance[0:3]
        balance_result = f"{balance_numbers}SEP"
        return balance_result
    else:
        return balance
