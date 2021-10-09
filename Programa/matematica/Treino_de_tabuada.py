import random
from time import sleep
from colorama import Fore, Style, init
import os

print('=================> treino de tabuada <=================')


def tabuada():
    print(f'~~~~~ tabuada do {ran1} ~~~~~')
    for nt in range(0,11):
        l[ran2] = f'{Fore.GREEN}{l[ran2]}{Style.RESET_ALL}'
        print(f'{ran1} x {nt} = {l[nt]}')
    print(f'~~~~~~~~~~~~~~~~~~~~~~')
while True:
    init()
    l=[]
    ran1 = random.randrange(1,11)
    ran2 = random.randrange(1,11)

    r = int(input(f'{ran1} x {ran2} = '))

    for i in range(0,11):
        t = i*int(ran1)
        l.append(t)

    if r == l[ran2]:
        print(f'{Fore.GREEN}CERTO{Style.RESET_ALL}')
        op = input('conferir tabuada?[S/N]: ').upper()
        while op not in 'SN':
            print('=== erro de digitação ===')
            op = input('conferir tabuada?[S/N]: ').upper()
        if op == 'S':
            tabuada()
            c=input('Quer continuar a treinar?[S/N]: ').upper()
            while c not in 'SN':
                print('=== Erro de digitação ===')
                c=input('Quer continuar a treinar?[S/N]: ').upper()
            
            if c=='N':
                break
            else:
                os.system('cls')
                print('=================> treino de tabuada <=================')         
           
        elif op == 'N':
            c=input('Quer continuar a treinar?[S/N]: ').upper()
            while c not in 'SN':
                print('=== Erro de digitação ===')
                c=input('Quer continuar a treinar?[S/N]: ').upper()
                print(c)
            if c=='N':
                break
            else:
                os.system('cls')
                print('=================> treino de tabuada <=================')         
              
    else:
        print(f'{Fore.RED}ERRADO{Style.RESET_ALL}')
        op = input('conferir tabuada?[S/N]: ').upper()
        while op not in 'SN':
            print('=== erro de digitação ===')
            op = input('conferir tabuada?[S/N]: ').upper()
        if op == 'S':
            tabuada()
            c=input('Quer continuar a treinar?[S/N]: ').upper()
            while c not in 'SN':
                print('=== Erro de digitação ===')
                c=input('Quer continuar a treinar?[S/N]: ').upper()
            if c=='N':
                break
            else:
                os.system('cls')
                print('=================> treino de tabuada <=================')         
        elif op == 'N':
            c=input('Quer continuar a treinar?[S/N]: ').upper()
            while c not in 'SN':
                c=input('Quer continuar a treinar?[S/N]: ').upper()
            if c=='N':
                break
            else:
                os.system('cls')
                print('=================> treino de tabuada <=================')

                



