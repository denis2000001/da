import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="Ok!")

async def tomorrow_bd():
    await bot.send_message(chat_id=chat_id, text="Hey,Hey,Tomorrow is ur birthday we're gone party like it's ur \
     birthday!")

async def bd():
    await bot.send_video(chat_id=chat_id, text="Happy birthday")

async def scheduler():
    aioschedule.every().year.at("09.03").do(tomorrow_bd)
    aioschedule.every().year.at("10.03").do(bd)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)