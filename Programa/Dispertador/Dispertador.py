import time
import os
from python_play.player import play_it


def horário():
    while True:
        def clear(): return os.system('cls')
        print('segure o botão do CTRL+C para despertar')
        print('Hora local:', end=' ')
        local = time.localtime()
        print(time.strftime('%H:%M:%S', local))
        time.sleep(1)
        clear()
        if list[0] == time.strftime('%H'):
            if list[1] == time.strftime('%M'):
                if list[2] == time.strftime('%S'):
                    break


h = input('Deseja despertar que horas (horas:min:seg): ')
print(f'parar em {h} segundos')
list = h.split(':')
horário()
play_it(r'')
