from aiogram.dispatcher.filters.state import StatesGroup, State


class Order(StatesGroup):
    size = State()
    payment = State()
    check = State()
