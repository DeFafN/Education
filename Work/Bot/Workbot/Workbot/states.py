from aiogram.fsm.state import StatesGroup, State

class FSM_event(StatesGroup):
    event_type = State()
    with_whom = State()
    name_with = State()
    when = State()
    speed = State()
    need_help = State()
    text = State()
    check = State()