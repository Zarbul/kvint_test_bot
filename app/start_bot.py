from aiogram.utils import executor

from create_bot import dp


from handlers import button_handler, message_handler

button_handler.register_button_handlers(dp)
message_handler.register_message_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
