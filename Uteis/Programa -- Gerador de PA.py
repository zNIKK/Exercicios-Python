from os import system
while True:
    ter=int(input('Primeiro termo: '))
    raz=int(input('Razão da PA: '))
    dec=ter+(10-1)*raz
    for n in range(ter,dec+raz,raz):
        print(n, end='')
        print(' = END ' if n==dec else ' -> ',end=' ')
    c=input('\nQuer continuar?[S/N]: ').upper()
    while c not in 'SN':
        c=input('Quer continuar?[S/N]: ').upper()
    if c=='N':
        break
    else:
        system('cls')

    

