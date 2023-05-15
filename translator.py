import translators as ts
import app
from app import Task, doneQueue

a = '你好啊~'
b = "Do you know how to code? You're not good? Why am I"

def ta(end):
    trans = ts.translate_text(a, end, app.lang, 'en', timeout = 5, proxies = app.proxies)
    if len(trans) > len(a):
        print(f'{end}: {trans}')

def tb(end):
    trans = ts.translate_text(b, end, 'en', app.lang, timeout = 5, proxies = app.proxies)
    if len(trans) > len(b):
        print(f'{end}: {trans}')

for (end, output) in doneQueue([(end, Task(Task(ta,(end,)).catch)) for end in ts.translators_pool]):
    pass

for (end, output) in doneQueue([(end, Task(Task(tb,(end,)).catch)) for end in ts.translators_pool]):
    pass