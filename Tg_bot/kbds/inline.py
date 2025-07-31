from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Нажми сюда, чтобы узнать, что я умею',
                          callback_data='help')],
])


# class MenuCallBack(CallbackData, prefix='menu'):
#     level: int
#     menu_name: str
#     category: int | None = None
#     page: int = 1
#     product_id: int | None = None


# def weekdays(*, level: int, categories: list, sizes: tuple[int] = (2,)):
#     builder = InlineKeyboardBuilder()
