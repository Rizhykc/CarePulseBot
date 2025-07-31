from datetime import datetime

from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter, or_f, callback_data

from aio_calendar import SimpleCalendar, get_user_locale
from aio_calendar.schemas import SimpleCalendarCallback
# from filters.chat_types import ChatTypeFilter, IsAdmin
from kbds import reply as kb

# import conts

user_router = Router()


@user_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name},',
                         reply_markup=kb.start_kb)


@user_router.message(F.text.lower() == 'navigation calendar')
async def calendar_start(message: types.Message):
    await message.answer(
        'Вот', reply_markup=await SimpleCalendar(
            locale=await get_user_locale(message.from_user)
        ).start_calendar()
    )


@user_router.callback_query(SimpleCalendarCallback.filter())
async def process_simple_calendar(
    callback_query: types.CallbackQuery,
    callback_data: callback_data.CallbackData
):
    calendar = SimpleCalendar(
        locale=await get_user_locale(callback_query.from_user),
        show_alerts=True
    )
    calendar.set_dates_range(datetime(2025, 1, 1), datetime(2030, 12, 31))
    selected, date = await calendar.process_selection(
        callback_query,
        callback_data
    )
    if selected:
        await callback_query.message.answer(
            f'You selected {date.strftime("%d/%m/%Y")}',
            reply_markup=kb.start_kb
        )


@user_router.callback_query(F.data == 'reminders')
async def reminders_call(callback: types.CallbackQuery):
    await callback.answer('', reply_markup=kb.reminders)


@user_router.message(F.text.lower() == '')
async def answer_filter(message: types.Message):
    pass
