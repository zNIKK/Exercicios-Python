num=int(input('numero:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade={}\tDezena={}\tCentena={}\tMilhar={}'.format(u,d,c,m))
