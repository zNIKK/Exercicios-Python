from decimal import Decimal
from os import system
while True:
    peso=float(input('Qual o seu peso (Kg):'))
    altu=float(input('Qual a sua altura (M):'))

    conta=peso/(altu*altu)
    IMC=Decimal('%.2f'%conta)
    if IMC < 18.5:
        print('você está ABAIXO DO PESO // PESO:{}'.format(IMC))
    elif IMC > 39.9:
        print('você está com OBESIDADE GRAVE // PESO:{}'.format(IMC))
    elif 30 >= IMC < 39.9:
        print('você está com OBESIDADE // PESO:{}'.format(IMC))
    elif 25 >= IMC < 29.9:
        print('você está com SOBREPESO // PESO:{}'.format(IMC))
    elif 18.5 >= IMC < 24.9:
        print('você está no PESO IDEAL // PESO:{}'.format(IMC))
    c=input('\nQuer continuar?[S/N]: ').upper()
    while c not in 'SN':
        c=input('Quer continuar?[S/N]: ').upper()
    if c=='N':
        break
    else:
        system('cls')


