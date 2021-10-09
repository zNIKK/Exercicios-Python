dict={}
list=[]

dict['nome']=input('Nome: ')
dict['media']=float(input(f'Média do {dict["nome"]}: '))
list.append(dict.copy())
print('-='*15)
for i in list:
    for k,v in i.items():
        print(f'{k} é igual a {v}')
    if dict['media']<=5:
        print(f'{k} foi REPROVADO')
    elif dict['media']<7:
        print(f'{k} ficou de RECUPERAÇÃO')
    elif dict['media']>=7:
        print(f'{k} foi APROVADO')
