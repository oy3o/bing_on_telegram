import config
import httpx
import os
import signal
import time
from urllib.parse import parse_qs
import app
import botpy

app.bot_id = config.qq_bot_id
app.bot_name = config.qq_bot_name
app.admin_id = config.qq_admin_id
app.admin_channel = config.qq_admin_channel
app.admin_name = config.qq_admin_name

bot = None
post = httpx.Client(headers={'Authorization': f'Bot {app.bot_id}.{config.qq_bot_token}'}).post

async def _receive(message):
    app.bot_id = (await bot.api.me()).id if not app.bot_id else app.bot_id
    await app.receive(message.channel_id, message.author.id, message.author.username, message.id, message.content)
async def _bot_send(chatid, msg, forward, *, suggest_reply, connect_timeout):
    # 上线 api url: https://api.sgroup.qq.com/ 
    return parse_qs(post(f'https://sandbox.api.sgroup.qq.com/channels/{chatid}/messages',data={'content': msg, 'msg_id': forward}).text)['id'][0]
async def _bot_stop():
    os.kill(os.getpid(), signal.SIGINT)

app.bot_send = _bot_send
app.bot_stop = _bot_stop
app.init()

class QQ(botpy.Client):
    async def on_direct_message_create(self, message):
        await _receive(message)
    async def on_message_create(self, message):
        await _receive(message)

print(time.ctime(), 'app running on QQ bot...')
bot = QQ(intents=botpy.Intents(guild_messages=True, direct_message=True))
bot.run(appid=app.bot_id, token=config.qq_bot_token)