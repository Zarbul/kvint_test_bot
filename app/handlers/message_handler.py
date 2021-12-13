from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from app.handlers.state.state import Order


async def size(message: types.Message):
    await message.reply(
        "Какую вы хотите пиццу? Большую или маленькую?",
    )

    await Order.size.set()


async def payment(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await message.reply(
        "Как вы будете платить? Картой или наличными?",
    )
    await Order.next()


async def check(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['payment'] = message.text
        await message.reply(
            f"Вы хотите {data['size']} пиццу, оплата - {data['payment']}?\n"
            f"Если все верно, введите 'верно'.\n"
            f"Если Вы ошиблись, нажмите кнопку 'Отмена' и начните заново.",
        )
    await Order.next()


async def submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['check'] = message.text
        await message.reply(
            f"Заказ на {data['size']} пиццу, оплата - {data['payment']} принят.\n"
            f"Приятного аппетита",
        )
    await state.finish()


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(size, Text(equals="Заказать пиццу", ignore_case=True), state=None)
    dp.register_message_handler(payment, state=Order.size)
    dp.register_message_handler(check, state=Order.payment)
    dp.register_message_handler(submit, Text(equals="верно", ignore_case=True), state=Order.check)
