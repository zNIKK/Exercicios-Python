import time
maior=0

num1=int(input('Primeiro número:'))
num2=int(input('Segundo número:'))
repeat=True
while repeat:
    print('\t[ 1 ] Somar\n'
          '\t[ 2 ] mutiplicar\n'
          '\t[ 3 ] maior\n'
          '\t[ 4 ] novos números\n'
          '\t[ 5 ] sair do programa')
    op=int(input('>>>>> Qual é a sua opção? '))
    if op==1:
        to=num1+num2
        print('A soma entre {} + {} é {}'.format(num1,num2,to))
        print('==-'*12)
        time.sleep(2)
    if op==2:
        to1=num1*num2
        print('A multiplicação entre {} * {} é {}'.format(num1,num2,to1))
        print('==-'*12)
        time.sleep(2)

    if op==3:
        if num1 > num2:
            maior=num1
            print('entre {} e {} o número {} é o maior'.format(num1,num2,maior))
            print('==-' * 12)
            time.sleep(2)

        elif num1 < num2:
            maior=num2
            print('entre {} e {} o número {} é o maior'.format(num1,num2,maior))
            print('==-' * 12)
            time.sleep(2)

    if op==4:
            num1=int(input('Primeiro número:'))
            num2=int(input('Segundo número:'))
    if op==5:
        repeat=False



