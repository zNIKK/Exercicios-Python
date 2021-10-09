op='S'
while op=='S':
    n=int(input('Digite um valor: '))
    op=input('Quer continuar? [S/N]: ').upper()
    if n%2==0:
        print('------------------')
        print('Este número é PAR')
        print('------------------')
    else:
        print('------------------')
        print('Este número é IMPAR')
        print('------------------')
