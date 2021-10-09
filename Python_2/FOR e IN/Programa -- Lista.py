nomes=('nicolas','livia','vitoria')

print(len(nomes))

nome=input('Por favor, escreva o seu nome aqui\n')

if nome == 'nicolas':
        print('Bem Vindo!!!\n')
        for i in nomes:
            print(i)
elif nome == 'livia':
        print('bem vindo!!!\n')
        for i in nomes:
            print(i)
elif nome == 'vitoria':
    print('bem vindo!!!\n')
    for i in nomes:
        print(i)
else:
    print('desculpe, o seu nome não esta na lista ')

