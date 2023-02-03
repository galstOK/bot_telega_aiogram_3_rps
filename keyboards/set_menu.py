from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from lexicon.lexicon_ru import LEXICON_COMMANDS_RU



#Асинхронная функция для вывода кнопки меню
async def set_main_menu(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand(command=command, description=description) for command, description in LEXICON_COMMANDS_RU.items()
        ],
        scope=BotCommandScopeDefault()
    )