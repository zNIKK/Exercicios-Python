from time import sleep
def thread(txt):
    tam=len(txt)+3
    print('~'*tam)
    print(f' {txt}')
    print('~'*tam)
def ajuda():
    thread('SISTEMA DE AJUDA PyHELP')
    h=input('Função blibioteca >>> ')
    if not h=='fim':
        print(f'Organizando Blibioteca {h}...')
        sleep(2)
        print('=='*35)
        help(h)
        print('=='*35)
        sleep(1)
    return h

while True:
    h=ajuda()
    if h=='fim':
        break
thread('ATÉ LOGO!!!')
