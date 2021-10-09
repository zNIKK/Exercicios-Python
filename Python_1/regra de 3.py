print('1-diretamente proporcional\n2-inversamente proporcional')
escolha=input('escolha 1 ou 2:')
if escolha=='1':
    print('===========Diretamente proporcional===========')

    unid1=input('qual o nome da unidade de medida:')
    unid2=input('qual é o objeto:')

    num1=int(input('se:'))
    num2=int(input('faz em:'))
    num3=int(input('quantos:'))

    prod=num2*num3
    result=prod/num1
    print('\n')
    print(num1,unid1,'esta para',num2,unid2)
    print('ASSIM COMO:')
    print(num3,unid1,'esta para',result,unid2)

if escolha == '2':
    print('===========Inversamente proporcional===========')

    unid1 = input('qual o nome da unidade de medida:')
    unid2 = input('qual é o objeto:')

    num1 = int(input('se:'))
    num2 = int(input('faz em:'))
    num3 = int(input('quantos:'))

    prod = num1 * num2
    result = prod / num3
    print('\n')
    print(num1, unid1, 'esta para', num2, unid2)
    print('ASSIM COMO:')
    print(num3, unid1, 'esta para', result, unid2)