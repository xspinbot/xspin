from django.db import models

class LanguageType(models.TextChoices):
    uz = "uz", "Узбекский"
    ru = "ru", "Русский"

class GameType(models.TextChoices):
    basketball = "basketball", "Баскетбол"
    football = "football", "Футбол"
    dart = "dart",  "Дарт"
    game_die = "game_die", "Игровой кубик"
    bowling = "bowling", "Боулинг"
    slot_machine = "slot_machine", "Игровой автомат"

class AdminType(models.TextChoices):
    supervisor = "1", "Руководитель"
    junior_admin = "2", "Младший админ"
    admin = "3", "Админ"
    ceo = "4", "Генеральный директор (CEO)"

class TransferType(models.TextChoices):
    increase = "increase", "Увеличивать (+)"
    decrease = "decrease", "Снижаться (-)"