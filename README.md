# bing_on_telegram
通过tg来访问AI接口，因为AI模型有token限制，本项目提供个性化的会话保存功能

## run app
```
pip install -r requirements.txt
python -m app --workspace /path/to/save/ --token Telegram_BOT_TOKEN --name @botname --admin Telegram_USER_ID
```
## command  in telegram 
```
_1 - 群组功能
start - 在此开始监听 /start
reset - 重置群组上下文 /reset
ban - 用户禁用机器人 /ban username
free - 用户解除禁用 /free username
img - 生成图片 /img prompt
_2 - AI 列表（添加需选中角色和记忆）
list - 显示 AI 列表 /list
on - 启动 AI /on [bot1 bot2 bot3 = *]
off - 关闭 AI /off [bot1 bot2 bot3 = *]
set - 设置活跃 AI /set [bot1 bot2 bot3 = None]
add - 添加 AI /add name model cookie
remove - 移除 AI /remove name
mod - 修改AI /mod name [model [cookie]]
_3 - 会话功能（自动保存）
save - 保存上下文 /save
restore - 恢复上下文 /restore [auto=False]
warn - 显示模型提示错误 /warn
search - 显示过滤搜索结果 /search [query='']
auto - 机器人自动运行 /auto [times=5]
_4 - 会话列表
chat - 显示会话内容 /chat [name=this]
chatlst - 显示列表 /chatlst
chatadd - 添加会话 /chatadd name description [context=this]
chatmod - 修改会话 /chatmod name description [context=this]
chatdel - 删除会话 /chatdel chat_name
chatset - 选中会话 /chatset chat_name
_5 - 角色列表
role - 显示角色prompt /role [name=this]
rolelst - 显示角色列表 /rolelst
roleset - 选中角色 /roleset [c1 c2 c3 = None]
roleadd - 添加角色 /roleadd name description prompt
roledel - 移除角色 /roledel name
rolemod - 修改角色 /rolemod name [description [prompt]]
_6 - 记忆列表
mem - 显示记忆prompt /mem [name=this]
memlst - 显示记忆列表 /memlst
memset - 选中记忆 /memset [c1 c2 c3 = None]
memadd - 添加记忆 /memadd name description prompt
memdel - 移除记忆 /memdel name
memmod - 修改记忆 /memmod name [description [prompt]]
```
## build token count function (x86_64 linux version)
```bash
python -m pip install pyo3
python -m pip install maturin
maturin build --release -i 3.9 -b pyo3 --target "x86_64-unknown-linux-gnu"
pip install target/wheels/tokcos-0.3.4-cp39-cp39-manylinux_2_28_x86_64.whl
# change _tiktoken to _tokcos in tiktoken/core.py
```


