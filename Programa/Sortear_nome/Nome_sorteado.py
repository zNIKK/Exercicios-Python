import random

no1=input('escolha o primeiro nome:')
no2=input('escolha o segundo nome:')
no3=input('escolha o terceiro nome:')
no4=input('escolha o quarto nome:')

list=[no1,no2,no3,no4]

print('o nome escolhido é:',random.choice(list))