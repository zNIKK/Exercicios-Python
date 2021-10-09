listmai=[]
listmen=[]
cont=mai=men=nome=nome1=0
while True:
    n=input('Nome: ')
    p=float(input('Peso: '))
    c=' '
    cont+=1
    if cont==1:
        mai=men=p
        nome = listmai
        nome1=listmen
        if p>=mai:
            listmai.append(n)
        else:
            listmen.append(n)
    else:
        if p>=mai:
            mai=p
            listmai.append(n)
            nome = listmai

        elif p<=men:
            men=p
            listmen.append(n)
            nome1 = listmen


    while c not in 'NnSs':
        c=input('Quer continuar? [S/N]: ').upper()
    if c=='N':
        break

print(f'Ao todo você cadrastrou {cont} pessoas')
print(f'O maior peso foi de {mai} e foi da pessoa {nome}')
print(f'O menor peso foi de {men} e foi da pessoa {nome1}')