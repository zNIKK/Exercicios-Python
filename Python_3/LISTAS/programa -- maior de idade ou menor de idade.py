pessoal=[]
dado=[]
mai=men=0
for i in range(0,3):
    dado.append(input('Nome:'))
    dado.append(int(input('Idade:')))
    pessoal.append(dado[:])
    dado.clear()
for p in pessoal:
    if p[1]>=18:
        print(f'o {p[0]} é MAIOR de idade')
        mai+=1
    else:
        print(f'o {p[0]} é MENOR de idade')
        men+=1
print(f'Temos {mai} maiores de idade e {men} menores de idade')
