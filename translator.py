import translators as ts
import app
from app import Task, doneQueue

a = '你好~你会代码吗？你不好？我是？我不是？对对对？原神。。。原原原，我你，还行吧这样，还行吧，好像，我觉得，我认识他好像'
b = "Hello~ Can you code? You're not good? I am? I'm not? Yeah? Genshin. . . Yuanyuanyuan, me and you, are you okay like this, are you okay, like, I think, I know him like"

def ta(end):
    trans = ts.translate_text(a, end, app.lang, 'en', timeout = 5, proxies = app.proxies)
    if len(trans) > (len(a)/4):
        print(f'{end}: {trans}')

def tb(end):
    trans = ts.translate_text(b, end, 'en', app.lang, timeout = 5, proxies = app.proxies)
    if len(trans) > (len(b)/4):
        print(f'{end}: {trans}')

for (end, output) in doneQueue([(end, Task(Task(ta,(end,)).catch)) for end in ts.translators_pool]):
    pass

for (end, output) in doneQueue([(end, Task(Task(tb,(end,)).catch)) for end in ts.translators_pool]):
    pass