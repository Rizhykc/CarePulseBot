from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_inline = InlineKeyboardMarkup(
    InlineKeyboardButton(text='', callback_data=''),
    InlineKeyboardButton(text='', callback_data=''),
)


class MenuCallBack(CallbackData, prefix='menu'):
    level: int
    menu_name: str
    category: int | None = None
    page: int = 1
    product_id: int | None = None


def weekdays(*, level: int, categories: list, sizes: tuple[int] = (2,)):
    builder = InlineKeyboardBuilder()
