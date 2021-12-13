from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


reg_button = KeyboardButton("Заказать пиццу")
cancel_button = KeyboardButton("Отмена")

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(reg_button).insert(cancel_button)
