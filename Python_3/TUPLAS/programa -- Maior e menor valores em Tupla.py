import random
maior=0
menor=0
print('Os valores sorteados foram:', end=' ')
for r in range(0,5):
    rand=random.randint(0,10)
    tupla=print((rand),end=' ')
    if r==0:
        maior=rand
        menor=rand
    else:
        if rand>maior:
            maior=rand
        if rand<menor:
            menor=rand
print(f'\nO maior valor é {maior}\ne o menor valor foi {menor}')