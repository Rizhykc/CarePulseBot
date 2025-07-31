from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from filters.chat_types import ChatTypeFilter, IsAdmin
from kbds import reply as kb

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())


@admin_router.message(Command('admin'))
async def admin_features(message: types.Message):
    await message.answer('Что хотите сделать?', reply_markup=kb.main_admin)


# kb = [
#     [
#         keybutt(text='Посмотреть контент'),
#         keybutt(text='Добавить котика'),
#     ]
# ]

# main_admin = ReplyKeyboardMarkup(
#     keyboard=kb,
#     resize_keyboard=True,
#     input_field_placeholder='Что Вас интересует?'
# )

# inline_admin = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Изменить', callback_data='update'),
#      InlineKeyboardButton(text='Удалить', callback_data='delete')],
# ])
