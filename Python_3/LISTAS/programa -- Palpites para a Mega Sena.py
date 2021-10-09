import random
import time
print('--'*15)
print(f'{"MEGA SENA":^30}')
print('--'*15)

list=[]

r = int(input('Quantos jogos você quer sortear?: '))
print('-='*5,end=' ')
print(f'SORTEANDO {r} JOGOS',end=' ')
print('-='*5)
for i in range(1,r+1):
    list.clear()
    for j in range(0,6):
        rand = random.randint(1, 60)
        list.append(rand)
        list.sort()

    print(f'jogo {i}: {list}')
    time.sleep(1)
print('-='*5,end=' ')
print('< BOA SORTE >',end=' ')
print('-='*5,end=' ')
