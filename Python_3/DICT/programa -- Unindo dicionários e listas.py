dict={}
list=[]
cont=0
s=0
while True:
    dict['nome']=input('Nome: ')
    dict['sexo']=input('Sexo [M/F]: ').upper()
    cont+=1
    while dict['sexo'] not in 'MF':
        print('OPÇÃO INVALIDA!!! digite apenas M ou F')
        dict['sexo']=input('Sexo [M/F]: ').upper()
    dict['idade']=int(input('Idade: '))
    list.append(dict.copy())
    c=input('Quer continuar? [S/N]: ').upper()
    while c not in 'NS':
        print('OPÇÃO INVALIDA!!! digite apenas S ou N')
        c = input('Quer continuar? [S/N]: ').upper()
    if c=='N':
        break
v=0
for i in range(0,cont):
    s+=list[i]['idade']
    media=s/cont

print(f'=> Ao todo temos {cont} pessoas cadastradas')
print(f'=> A média de idade é de {media}')
print(f'=> As mulheres cadrastradas são',end=' ')
for e in range(0,cont):
    if list[e]['sexo']=='F':
        print(f'{list[e]["nome"]}',end=' ')
print()
print('=> Lista de pessoas acima da media:')
co=0
for a in list:
    if a['idade']>=media:
        print('    ', end='')
        for k, v in a.items():
            print(f'    {k} = {v}',end='; ')
        print()

print('<<< ENCERRADO >>>')