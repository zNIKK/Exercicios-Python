dict={}
list=[]
t=0
dict['nome']=input('Nome do Jogador: ')
dict['partidas']=int(input(f'Quantas partidas {dict["nome"]} jogou: '))
for i in range(0,dict['partidas']):
    list.append(int(input(f'\tQuantos gols na partida {i}: ')))
    dict['gols']=list[:]
for i in list:
    t+=i
    dict['total']=t
print('-='*30)
print(dict)
print('-='*30)
for k,v in dict.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {dict["nome"]} jogou {dict["partidas"]} partidas:')
for e,i in enumerate(list):
    print(f'\t=> Na partida {e}, fez {i} gols.')
print(f'Foi um total de {dict["total"]} gols.')
