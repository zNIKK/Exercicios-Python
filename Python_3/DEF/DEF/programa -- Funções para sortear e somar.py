from random import randint
from time import sleep

def sortear(list):
    for i in range(0,5):
        rand = randint(0, 10)
        list.append(rand)
    print('Sorteando 5 valores da lista ',end='')
    for n in list:
        print(f'{n}',end=' ')
        sleep(0.3)
    print('PRONTO')


def sompar(list):
    s=0

    for n in list:
        if n%2==0:
            s+=n
    print(f'somando os pares de {list}, temos {s}')


list=[]
sortear(list)
sompar(list)