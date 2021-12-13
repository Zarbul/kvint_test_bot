import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from pymongo import MongoClient

import config


TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
storage = MemoryStorage()
# storage = RedisStorage2(
#     host=config.REDIS_HOST,
#     port=config.REDIS_PORT,
    # db=config.REDIS_DB,
    # password=config.REDIS_PASSWORD,
# )
cluster = MongoClient(
    f"mongodb+srv://{config.MONGO}",
    # ssl=True,
    # ssl_cert_reqs='CERT_NONE'
)
db = cluster["testDB"]
workers = db["testWorker"]

dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())