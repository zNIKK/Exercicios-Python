num1=int(input('Primeiro número:'))
num2=int(input('Segundo número:'))

if num1 > num2:
    print('o numero {} é o maior'.format(num1))
elif num2 > num1:
    print('o numero {} é o maior'.format(num2))
elif num1 == num2:
    print('os dois números são iguais')