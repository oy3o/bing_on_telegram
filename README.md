# Running New Bing & Bard on Telegram(or others e.g. QQ) can save chats at the same time
*[简体中文](README-zh.md)*

Access to different artificial intelligences via Telegram. Since the model has token restrictions, the purpose of this project is to allow AI to remember more important memories, and provide the ability to play roles and save sessions.

At present, it is possible to realize simultaneous dialogue between different AIs in the same chat window, more intelligent information segmentation, perfect error prompts and search display.

If you want to use another platform's bot instead of telegram bot, you can do it in less than 50 lines of code (you can check the code of both telegram and QQ platforms).

## configuration file`config.py`
- `workspace`: `'/path/to/save/data'` where your data is stored
- `once`: `True|False` Whether to enable a reply once, no longer intelligently split the answer of bing
- `lang`: `'zh'|'ru'|...` google bar currently only supports English, you can set it to your favorite language, and the program will translate between you (the first time you need to download it, please wait)
- `proxies`: `proxies = {'https://': 'http://127.0.0.1:1081'}` proxy, if your network condition is not good, you can configure the proxy format as
- `bot_command_start`: `'/'` This is an idea, let Ai itself call the command, which can be used in image generation and other places
- `auto_mention`: `'(auto response)'` is also an idea, let AI run automatically through automatic reply, give a task and let it run continuously, and then call the command to end by itself.
- `bot_id | bot_token | admin_id | admin_channel`: These are obtained through the platform, please search for the telegram bot application and the qq robot application.
- `bot_name`: only affects group chat, for example, `bot_name` can be set to `'hi'`, so that when a group friend's message starts with `'hi'`, it will be responded.
- `admin_name`: just the name you saved in the file, it would be too strange if they are all called user, imagine your role is a lover, and then your messages all carry user.

## Run the application
```
# enter to project directory
pip install -r requirements.txt
python -m tg # command to start telegram bot
python -m qq # command to start QQ bot
```
*It should be noted that the api address of the qq robot is different from that in the test phase, it has been commented in qq.py, please modify it according to your needs*

## Run a normal Bing bot
```
# Put your cookie file in workspace/cookie/
# Enter the code in Telegream
/add set name bing cookie file name
/on set name
```
- *Currently supported AI `bing`, `bard`*
- *You can start multiple AIs, even the same model with the same cookie*
- *Can be used in group chat, need to be set as administrator*


## run bing with a roleplay
```
# command in telegram
/roleadd role_name role_description role_prompt
/memadd memory_name(always a number) memory_description memory_prompt
# select both role and memory
/roleset role_name1 role_name2 role_name3
/memset 0 1 2 3 4
# add a ai that you can turn on it anytime anywhere
/add ai_name bing cookie_file_name
# turn on ai
/on ai_name
```
- *If there are many characters and memories, it is recommended to use number naming*
- *You can personalize the experience by combining different characters and memories*
- *For example, the character can be student+sister+magic girl, and the memory can be historical setting+related knowledge+what you have done*


## save and restore a chat
```
# save current to list
/chatadd chat_name chat_description
# then restore from list
/chatset chat_name
# or you can save temp
/save
# then restore from temp (This is for restarting the application settings. Generally, it will not be used.
# If there is an unexpected termination, it can be restored by /restore auto, because there is automatic saving)
/restore 
```
- *It is actually possible to have multiple threads by opening multiple chat channels instead of just saving to the list*
- *The session will record the current AI enabled status and session context*


## command in chat
```
_1 - group function
start - start listening here /start
reset - reset the group context /reset
mode - multi AI forward mode /mode [forward|withcontext]
ban - user to disable bots /ban username
free - user unbanned /free username
img - generate image /img prompt
_2 - AI list (add required characters and memories)
list - show AI list /list [update]
on - start AI /on [bot1 bot2 bot3 = *]
off - turn off AI /off [bot1 bot2 bot3 = *]
set - set active AI /set [bot1 bot2 bot3 = None]
add - add AI /add name model cookie
remove - remove AI /remove name
mod - modify AI /mod name [model [cookie]]
_3 - session function (autosave)
save - save the context /save
restore - restore context /restore [auto=False]
warn - display model prompts for errors /warn
search - show filtered search results /search [query='']
auto - the robot runs automatically /auto [times=5]
_4 - conversation list
chat - show chat content /chat [name=this]
chatlst - show list /chatlst
chatadd - add conversation /chatadd name description [context=this]
chatmod - modify session /chatmod name description [context=this]
chatdel - delete conversation /chatdel chat_name
chatset - Select conversation /chatset chat_name
chatfix - fix session /chatfix [context=this] #default is apply tg delete action
_5 - List of roles
role - show role prompt /role [name=this]
rolelst - show list /rolelst
roleset - selected roles /roleset [c1 c2 c3 = None]
roleadd - add a role /roleadd name description prompt
roledel - remove role /roledel name
rolemod - modify a role /rolemod name [description [prompt]]
_6 - memory list
mem - show memory prompt /mem [name=this]
memlst - show list /memlst
memset - selected memory /memset [c1 c2 c3 = None]
memadd - add memory /memadd name description prompt
memdel - remove memory /memdel name
memmod - modify memory /memmod name [description [prompt]]
```
- *`list [update]` is after you manually modify the files in the folder, you can automatically update the list by adding the `update` parameter*
- *Why not scan files automatically? Because the names in the design should all be numbers for quick input, different files can be distinguished by entering descriptions, and automatic scanning cannot generate descriptions*

## build token count function (x86_64 linux version)
```bash
python -m pip install pyo3
python -m pip install maturin
maturin build --release -i 3.9 -b pyo3 --target "x86_64-unknown-linux-gnu"
pip install target/wheels/tokcos-0.3.4-cp39-cp39-manylinux_2_28_x86_64.whl
# change _tiktoken to _tokcos in tiktoken/core.py
```


