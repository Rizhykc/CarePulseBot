from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton as keybutt
from aiogram.utils.keyboard import ReplyKeyboardMarkup

kb = [
    [
        keybutt(text='Календарь1'),
    ],
    [
        keybutt(text='Календарь2'),
    ],
]

start_kb = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
