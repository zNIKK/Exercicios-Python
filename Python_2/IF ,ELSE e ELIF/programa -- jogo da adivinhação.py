import random

random=random.randint(0,5)
print('--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
print('Tente adivinhar em um numero de 0 a 5')
print('--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
num=int(input('Em que numero eu pensei?: '))

if num==random:
    print('PARABÉNS! Você conseguiu acertar!')
else:
    print('GANHEI! Eu pensei no numero {} não no numero {}'.format(random,num))

