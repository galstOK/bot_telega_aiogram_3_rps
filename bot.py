import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from config_data.config import Config, load_config
from handlers.user_handlers import register_user_handlers
from handlers.other_handlers import register_other_handlers
from keyboards.set_menu import set_main_menu

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_other_handlers(dp)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s'
    )

    # Выводим в консоль информацию о начале запуска бота
    logging.info('Starting Bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Регистрируем все хэндлеры
    register_all_handlers(dp)

    # Вызов функции для создания меню
    await set_main_menu(bot=bot)

    # Запускаем polling
    try:
        await dp.start_polling(bot, skip_updates=True, on_startup=set_main_menu)

    finally:
        await bot.close()


if __name__ == '__main__':
    try:
        # Запускаем функцию main
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot Stopped')
