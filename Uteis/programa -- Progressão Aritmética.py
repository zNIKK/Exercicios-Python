ter=int(input('Primeiro termo: '))
raz=int(input('Razão da PA: '))
n=1
to=0
r=10
while r!=0:
    to+=r
    while n<=to:
        print('{} ->'.format(ter),end=' ')
        ter+=raz
        n+=1
    print(' = END')
    r=int(input('Quantos termos você vai querer mostrar?:'))
print('Finalizado com {} termos'.format(n))



