fat=int(input('Digite um número\npara calcular seu fatorial: '))
n=fat
to=1
print('Calculando o fatorial de {}! = {} x '.format(fat,fat),end='')
while not n==0:
    to*=n
    n-=1
    f=print('{}'.format(n),end=' ')
    print('x ' if n>0 else'= ',end='')
print(to)

