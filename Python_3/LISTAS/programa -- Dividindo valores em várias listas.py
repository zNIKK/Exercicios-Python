list=[]
par=[]
impar=[]
while True:
    v=int(input('Digite um número: '))
    c=' '
    list.append(v)
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
    while c not in 'SN':
        c=input('Quer continuar? [S/N] ').upper()
    if c=='N':
        break
print('-='*15)
print(f'A lista completa é {list}')
print(f'A lista de PARES é {par}')
print(f'A lista de IMPARES é {impar}')