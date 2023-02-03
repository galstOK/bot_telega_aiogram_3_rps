from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
kb_y_n = [
    [
        KeyboardButton(text=LEXICON_RU['yes_button']),
        KeyboardButton(text=LEXICON_RU['no_button'])
    ]
]

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
yes_no_kb = ReplyKeyboardMarkup(keyboard=kb_y_n,
                                one_time_keyboard=True,
                                resize_keyboard=True)

# Создаем игровую клавиатуру с кнопками "Камень 🗿", "Ножницы ✂" и "Бумага 📜"
# # Располагаем кнопки в клавиатуре одну под другой в 3 ряда
kb_game_main = [
    [
        KeyboardButton(text=LEXICON_RU['rock']),
        KeyboardButton(text=LEXICON_RU['scissors']),
        KeyboardButton(text=LEXICON_RU['paper'])
    ]
]

game_kb = ReplyKeyboardMarkup(keyboard=kb_game_main,
                              resize_keyboard=True)
