# New Bing & Bard on Telegram with chat save
*[简体中文](README.zh.md)*

Access different AI through telegram. Since the model has token restrictions, the purpose of this project is to let AI remember more important memories, and provide the ability to play roles and save sessions.

At present, it is possible to realize simultaneous conversations between different AIs in the same chat window, more intelligent information segmentation, perfect error prompts and search display.

If you want to use a bot from another platform instead of the telegram bot, you can implement it by modifying less than 50 lines of code under the Bot Initing block.

## run app
```
pip install -r requirements.txt
python -m app --workspace /path/to/save/ --token Telegram_BOT_TOKEN --name @botname --admin Telegram_USER_ID
```
- you can edit `config.py`, then run `python -m app` without arguments.
- you can also config your proxy in `config.py`

## start a bing bot
```
# put your cookie json in workspace/cookie/
# then input command in telegram
/add bot bing cookie.json
/on bot
```
**You can start multiple AIs, even the same model with the same cookie**
**It can be used in group chat, it needs to be set as an administrator, the name set by the prefix such as `@bot_name` can be responded, the administrator does not need**

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
**If there are many characters and memories, it is recommended to use number naming**
**You can achieve a personalized experience by combining different characters and memories**
**For example, the character can be student+sister+magic girl, and the memory can be historical+knowledge+what you have done**

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
**In fact, you can open multiple chat channels to conduct multiple topics instead of just saving to the list**
**The session will record the current AI enabled status and session context**

## command  in telegram 
```
_1 - group function
start - start listening here /start
reset - reset the group context /reset
mode - multi AI forward mode /mode [forward|withcontext]
ban - user to disable bots /ban username
free - user unbanned /free username
img - generate image /img prompt
_2 - AI list (add required characters and memories)
list - show AI list /list
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
## build token count function (x86_64 linux version)
```bash
python -m pip install pyo3
python -m pip install maturin
maturin build --release -i 3.9 -b pyo3 --target "x86_64-unknown-linux-gnu"
pip install target/wheels/tokcos-0.3.4-cp39-cp39-manylinux_2_28_x86_64.whl
# change _tiktoken to _tokcos in tiktoken/core.py
```


