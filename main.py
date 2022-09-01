from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin, fsm_anketa, notification,inline
from database import bot_dp
import logging
import asyncio


async def on_startup():
    asyncio.create_task(notification.scheduler())
    bot_dp.sql_create()

client.register_handlers_client(dp)
callback.register__handlers_callback(dp)
admin.register_handler_admin(dp)
fsm_anketa.register_handlers_fsmanketa(dp)
notification.register_handler_notification(dp)
extra.register_handler_extra(dp)
inline.register_handler_inline(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)