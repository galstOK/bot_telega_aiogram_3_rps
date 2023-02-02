from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
# yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
kb_y_n = [
    [
        KeyboardButton(text=LEXICON_RU['yes_button']),
        KeyboardButton(text=LEXICON_RU['no_button'])
    ]
]
# button_yes: KeyboardButton = KeyboardButton(LEXICON_RU['yes_button'])
# button_no: KeyboardButton = KeyboardButton(LEXICON_RU['no_button'])

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
yes_no_kb = ReplyKeyboardMarkup(keyboard=kb_y_n,
                                 one_time_keyboard=True,
                                 resize_keyboard=True)

# Создаем игровую клавиатуру с кнопками "Камень 🗿", "Ножницы ✂" и "Бумага 📜"
# game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
#
# button_1: KeyboardButton = KeyboardButton(LEXICON_RU['rock'])
# button_2: KeyboardButton = KeyboardButton(LEXICON_RU['scissors'])
# button_3: KeyboardButton = KeyboardButton(LEXICON_RU['paper'])
#
# # Располагаем кнопки в клавиатуре одну под другой в 3 ряда
# game_kb.add(button_1).add(button_2).add(button_3)
kb_game_main = [
    [
        KeyboardButton(text=LEXICON_RU['rock']),
        KeyboardButton(text=LEXICON_RU['scissors']),
        KeyboardButton(text=LEXICON_RU['paper'])
    ]
]

game_kb = ReplyKeyboardMarkup(keyboard=kb_game_main,
                              resize_keyboard=True)
