print('--'*15)
print('CADASTRE UMA PESSOA')
print('--'*15)
maior=menor=m=f=0

while True:
    i=int(input('Idade: '))
    s=' '
    c=' '
    while s not in 'MmFf':
        s=input('Sexo: [M/F] ').upper()
    while c not in 'SsNn':
        c=input('Quer cadastrar mais alguem? [S/N]: ')
    if i>=18:
        maior+=1
    elif i<18:
        menor+=1
    if s == 'm':
        m += 1
    elif s == 'f':
        f += 1
    if c=='n':
        break
print('Ao todo tem {} pessoas MAIORES DE IDADE e {} pessoas MENORES DE IDADE\n'
      'Ao todo temos {} HOMENS e {} MULHERES cadastrados'.format(maior,menor,m,f))