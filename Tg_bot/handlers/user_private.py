from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from filters.chat_types import ChatTypeFilter, IsAdmin
from kbds import inline as kb
import Tg_bot.conts as txt

user_router = Router()


@user_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}, {txt.TEXT}',
                         reply_markup=kb.menu_inline)


@user_router.callback_query(F.data == 'reminders')
async def reminders_call(callback: types.CallbackQuery):
    await callback.answer('', reply_markup=kb.reminders)
