n=z=u=0

n=int(input('Digite um número [999 para parar]: '))
while not n==999:
    u+=n
    z+=1
    n=int(input('Digite um número [999 para parar]: '))



print('A soma entre {} números foi de {}'.format(z,u))
