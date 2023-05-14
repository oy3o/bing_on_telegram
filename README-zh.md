# Telegram 上运行 New Bing & Bard 同时可以保存聊天
通过电报访问不同的人工智能。 由于模型有token限制，本项目的目的是让AI记住更重要的记忆，并提供角色扮演和session保存的能力。

目前可以在同一个聊天窗口实现不同AI之间的同时对话，更智能的信息切分，完善的错误提示和搜索展示。

如果你想使用另一个平台的机器人而不是电报机器人，你可以通过修改 `Bot Initing` 块下不到 50 行的代码来实现它。
## 运行应用
```
pip install -r requirements.txt
python -m app --workspace /path/to/save/ --token Telegram_BOT_TOKEN --name @botname --admin Telegram_USER_ID
```
- 您可以编辑 `config.py`，然后不带参数运行 `python -m app`。
- 你也可以在 `config.py` 中配置你的代理
- 您可以配置`lang`来访问 bard，而不是通过英语，例如 `lang = 'zh'`
- 您可以配置`once`以在一条消息中接收 bing 消息 `once = True`

## 运行一个普通的 Bing 机器人
```
# 将你的 cookie 文件放入 workspace/cookie/
# 在 Telegream 输入代码
/add 设定名字 bing cookie文件名字
/on 设定名字
```
**你可以启动多个AI，即使是同一个cookie同一个模型**

**可以在群聊中使用，需要设为管理员，通过前缀设定的名字如`@bot_name`可以被响应，管理员不需要**


## 运行一个角色扮演的机器人
```
# 在 Telegream 输入代码
/roleadd 角色名称 角色描述 角色prompt
/memadd 记忆名称 记忆描述 记忆prompt
# 然后选中添加的角色和记忆
/roleset 角色1 角色2 角色3
/memset 0 1 2 3 4
# 选中记忆后我们可以添加机器人，以便以后我们在任意地方启动
/add 机器人名称 bing cookie文件名字
# 然后是启动它，这样它就开始监听你当前的消息了
/on 机器人名称
```
**如果角色和记忆很多，推荐使用编号命名**

**你可以通过组合不同的角色和记忆达到个性化的体验**

**如角色可以是 学生+妹妹+魔法少女，记忆可以是 历史设定+相关知识+你们做了什么**


## save and restore a chat
```
# 保存当前会话到列表
/chatadd 会话名称 会话描述 [可选的不是当前会话，而是手动输入，可以通过chatcat查看当前会话]
# 从会话列表恢复
/chatset 会话名称
# 或者临时保存
/save
# 然后恢复 (这里是为了重启应用设置的，一般情况不会使用，出现意外终止可以通过 /restore auto 来进行恢复，因为存在自动保存)
/restore
```
**事实上可以通过开启多个聊天频道来进行多个话题而不只是保存到列表**

**会话会记录当前的 AI 开启状况和会话上下文**


## command  in telegram 
```
_1 - 群组功能
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
_3 - session functionality (autosave)
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


## 计算 token 的函数 count 需要手动编译，可以不编译，但是计数是在 python 进行，而不是 rust 会比较慢 (x86_64 linux version)
```bash
python -m pip install pyo3
python -m pip install maturin
maturin build --release -i 3.9 -b pyo3 --target "x86_64-unknown-linux-gnu"
pip install target/wheels/tokcos-0.3.4-cp39-cp39-manylinux_2_28_x86_64.whl
# change _tiktoken to _tokcos in tiktoken/core.py
```


