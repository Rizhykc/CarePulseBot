from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from filters.chat_types import ChatTypeFilter, IsAdmin
from kbds import as kb


admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())


@admin_router.message(Command("admin"))
async def admin_features(message: types.Message):
    await message.answer("Что хотите сделать?", reply_markup=kb.ADMIN_KB)
