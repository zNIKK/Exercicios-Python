dict={}
gols=[]
list=[]
t=0
while True:
    dict['nome']=input('Nome do jogador: ')
    dict['partidas']=int(input(f'Quantas partidas {dict["nome"]} jogou? '))
    for i in range(0,dict['partidas']):
        gols.append(int(input(f'Quantos gols na {i+1} partida: ')))
        dict['gols']=gols[:]
        t+=gols[i]
    dict['total']=t
    c=input('Quer continuar? [S/N]: ').upper()
    list.append(dict.copy())
    gols.clear()
    while c not in 'SN':
       print('ERRO! Digite apenas S ou N!')
       c=input('Quer continuar? [S/N]: ').upper()
    if c=='N':
        break
print('-='*25)
print(f'{"No.":<5}{"Nome":<14}{"gols":<30}{"total"}')
print('--'*25)
for i,e in enumerate(list):
     print(f'{i:<5}{e["nome"]:<14}{str(e["gols"]):<30}{e["total"]}')
print('-='*25)
while True:
    r=int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if r<=len(list)-1:
        print(f'-- LEVANTAMENTO DO JOGADOR {list[r]["nome"]}:')
        for c in range(0,len(list[r]["gols"])):
            print(f'No jogo {c+1} fez {list[r]["gols"][c]} gols')
        print('--' * 25)
    if r==999:
        break
    if r>len(list)-1:
        print(f'Não existe jogador {r}')