import random
from time import sleep
import operator
maior=0
menor=0
dict={}
list=[]

for i in range(1,5):
    rand=random.randint(0,5)
    dict[f'jogador {i}']=rand
for k,v in dict.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*15)
print(f'{"RANKING DOS JOGADORES":^30}')
print('-='*15)

ranking=sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
for i,r in enumerate(ranking):
    print(f'{i+1}º lugar: {r[0]} com {r[1]}')
    sleep(1)








