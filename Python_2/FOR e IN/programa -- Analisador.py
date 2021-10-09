maior=0
s=0
mulher=0
homem=0
p=0
sex=None
n=None
for i in range(1,5):
    print('--------{}ª Pessoa--------'.format(i))
    nome=input('Nome: ')
    idade=int(input('Idade: '))
    sexo=input('Sexo [M/F]: ')
    s+=idade
    if sexo=='M' or 'm':
        sex='O HOMEM mais velho'
        if sexo=='m':
            homem+=1
    if sexo=='F' or 'f':
        sex='A MULHER mais velha'
        if sexo=='f':
            mulher+=1
    else:
        print('Invalido!! Escolha seu sexo de nascença')
    if i==1:
        maior=idade
        n=nome
    else:
        if idade>maior:
            maior=idade
            n=nome
    if idade<18:
        p+=1

print('{} tem {} anos e se chama {}'.format(sex,maior,n))
print('A média da idade do grupo é de {} anos'.format(s/4))
print('Ao todo tem {} mulheres e {} homens e {} deles são menores de idade '.format(mulher,homem,p))