list=[]
cont=0
while True:
    v=(int(input('Digite um valor: ')))
    cont+=1
    c=' '
    if v not in list:
        list.append(v)
        print('ADCIONADO COM SUCESSO!!')
    else:
        print('VALOR INVALIDO! Não digite valores repitidos')
    while c not in 'SN':
        c=input('Quer continuar? [S/N] ').upper()
    if c=='N':
        break

print(f'você digitou: {list}')
