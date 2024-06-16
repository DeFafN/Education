from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, reply_keyboard_markup
from states import FSM_event
from aiogram.fsm.context import FSMContext

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(text.greeting.format(name=msg.from_user.full_name), reply_markup=kb.menu)
    await state.set_state(FSM_event.event_type)
@router.callback_query(F.data.in_({'succes', 'event', 'process', 'case', 'personal_event'}))
async def event_type (call: CallbackQuery, state: FSMContext):
    await state.update_data(event_type = call.message)
    await call.message.answer(text.is_it_you_question, reply_markup=kb.second_menu)
    await state.set_state(FSM_event.with_whom)

@router.callback_query(F.data.in_({'yes', 'colleague', 'other'}))
async def with_whom(call: CallbackQuery, state: FSMContext):
    await state.update_data(with_whom = call.message)
    if call.data == 'yes':
        await state.set_state(FSM_event.name_with)
        await call.message.answer(text.when_text)
        name = call.from_user.full_name
        await state.update_data(name_with = name)
        await state.set_state(FSM_event.when)
    elif call.data == 'colleague':
        await call.message.answer(text.colleague_name)
        await state.set_state(FSM_event.name_with)
    elif call.data == 'other':
        await call.message.answer(text.other_text)
        await state.set_state(FSM_event.name_with)

@router.message(FSM_event.name_with)
async def get_date(msg: Message, state: FSMContext):
    await msg.answer(text.when_text)
    await state.set_state(FSM_event.when)
    
@router.message(FSM_event.when)
async def get_date(msg: Message, state: FSMContext):
    await msg.answer((text.speed_text), reply_markup=kb.speed_menu)
    await state.set_state(FSM_event.speed)

@router.callback_query(F.data.in_({'yes', 'no'}))
async def event_type (call: CallbackQuery, state: FSMContext):
    await call.message.answer((text.need_help), reply_markup=kb.need_help_menu)
    await state.set_state(FSM_event.need_help)

@router.callback_query(F.data.in_({'have_text', 'need_edit', 'need_help'}))    
async def edit(call: CallbackQuery, state: FSM_event):
    edit = call.text
    if edit == 'need_help':
        await state.update_data(need_help = call.message)
        await call.answer(text.end)
               
    else:
        await state.update_data(need_help = call.message)
        await state.set_state(FSM_event.text)
        await call.answer(text.text)

@router.message(Command("stop"))
async def stop_handler(msg: Message):
    await msg.answer(text.buy)