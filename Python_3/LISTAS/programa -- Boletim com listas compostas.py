list=list()
while True:
    n=str(input('Nome: '))
    no1=float(input('Nota 1: '))
    no2=float(input('Nota 2: '))
    media =(no1+no2)/2
    list.append([n,[no1,no2],media])
    print(list)
    c=' '
    while c not in 'SsNn':
        c=input('Quer continuar? [S/N]: ').upper()
    if c=='N':
        break
print(f'{"No.":<5} {"NOME":<10} {"MÉDIA":>10}')
print('=='*15)
for i,a in enumerate(list):
    print(f'{i:<5}{a[0]:<10}{a[2]:>10}')
while True:
    r=int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if r<=len(list)-1:
        print(f'As notas de {list[r][0]} são {list[r][1]}')
    if r==999:
        break
print('>>>> VOLTE SEMPRE <<<<')


