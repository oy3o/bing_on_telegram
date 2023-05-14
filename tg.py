import asyncio
import config
import os
import signal
import time
import app
from app import AsyncTask
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, MessageHandler, filters

app.bot_id = config.tg_bot_id
app.bot_name = config.tg_bot_name
app.admin_id = config.tg_admin_id
app.admin_channel = config.tg_admin_channel
app.admin_name = config.tg_admin_name

bot = None

async def _update_edit(update, context):
    message = update.message
    await app.update_edit(message.chat.id, message.from_user.id, message.from_user.username, message.message_id, message.text)
async def _receive(update, context):
    message = update.message
    await app.receive(message.chat.id, message.from_user.id, message.from_user.username, message.message_id, message.text)

async def _bot_send(chatid, msg, forward, *, suggest_reply, connect_timeout):
    reply_markup = ReplyKeyboardMarkup(
            [[reply] for reply in suggest_reply],
            resize_keyboard=True,
            one_time_keyboard=True,
        ) if suggest_reply else ReplyKeyboardRemove()
    m = await bot.send_message(chatid, msg, reply_markup=reply_markup, connect_timeout=connect_timeout) 
    return m.message_id

async def _bot_stop():
    os.kill(os.getpid(), signal.SIGINT)

async def _isMessageExist(messageid, chatid):
    try:
        m = await bot.forward_message(chatid, chatid, messageid, True)
        await bot.delete_message(chatid, m.message_id)
        return True
    except:
        return False

app.bot_send = _bot_send
app.bot_stop = _bot_stop
app.isMessageExist = _isMessageExist
app.init()

tg = Application.builder().token(config.tg_bot_token).build()
tg.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, _update_edit))
tg.add_handler(MessageHandler(filters.TEXT, _receive))
bot = tg.bot

async def main():
    print(time.ctime(), 'app running on telegram bot...')
    app.bot_id = (await bot.get_me()).id
    await app.command('/start', app.admin_channel)
    await AsyncTask(tg.run_polling).retry(stop=lambda: not app.Running, onException=app.log)

asyncio.run(main())