ter=int(input('Primeiro termo: '))
raz=int(input('Razão da PA: '))
dec=ter+(10-1)*raz
for n in range(ter,dec+raz,raz):
    print(n, end='')
    print(' = END ' if n==dec else ' -> ',end=' ')
