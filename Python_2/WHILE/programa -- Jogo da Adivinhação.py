import random
n=0
print('\033[0;32mEstou pensando em um número...\033[m\n'
      'Tente advinhar o número de \033[0;32m0\033[m a \033[0;32m10')
rand=random.randint(0,10)
resp=0
while resp!=rand:
    resp=int(input('Qual o seu palpite?: '))
    n+=1
    if resp==rand:
        print('\033[0;32mParabéns!!!\033[m o número que eu pensei foi \033[0;32m{}\033[m\n\033[0;31mVocê acertou com {} tentativas'.format(rand,n))
    else:
        if rand>resp:
            print('\033[0;32mMais... \033[0;31mTente mais uma vez\033[m')
        elif rand<resp:
            print('\033[0;32mMenos... \033[0;31mTente novamente\033[m')