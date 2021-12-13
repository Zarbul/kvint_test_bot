from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from app.keyboard.buttons import keyboard


async def welcome(message: types.Message):
    await message.answer(
        f"Добро пожаловать, {message.from_user.username}!\n"
        f"Чтобы  сделать заказ, нажмите на кнопку 'Заказать пиццу'",
        reply_markup=keyboard,

    )


async def cancel(message: types.Message, state: FSMContext):
    await message.reply(
        "Заказ отменен.", reply_markup=keyboard
    )
    await state.finish()


def register_button_handlers(dp: Dispatcher):
    dp.register_message_handler(welcome, commands=['start', 'help'])
    dp.register_message_handler(cancel, Text(equals="Отмена"), state="*")