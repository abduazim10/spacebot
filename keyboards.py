from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboards.add(KeyboardButton('🧑‍🎓 Профиль'),KeyboardButton('🪙 Мои монеты'),KeyboardButton('💥 Space Shop'))
start_keyboards.add(KeyboardButton('🏫 О школе'),KeyboardButton('✍️ Оставить отзыв'))

start_keyboards2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton("Profil 👤")],
], resize_keyboard=True)

school_keyboards = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton('Философия школы', callback_data='schoolm_1'),
        InlineKeyboardButton('Преподователи', callback_data='schoolm_2'),
    ],
    [
        InlineKeyboardButton('Экскурсия по школе', callback_data='schoolm_3'),
        InlineKeyboardButton('Работы учеников', callback_data='schoolm_4'),
    ],
    [
        InlineKeyboardButton('Отзывы', callback_data='schoolm_5'),
    ]
])

otziv_keyboards = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton('8-10 лет', callback_data='otziv_1'),
        InlineKeyboardButton('14-16 лет', callback_data='otziv_2'),
    ]
])
