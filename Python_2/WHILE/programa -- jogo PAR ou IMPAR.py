import random
print('-='*15)
print('JOGO DO PAR OU IMPAR')
print('-='*15)
cont=0
while True:
    c = random.randint(0, 10)
    ip=' '
    while ip not in 'parimpar':
        ip = str(input('PAR ou IMPAR: ')).strip()
    v = int(input('Diz um valor: '))
    to=c+v
    print('-=' * 15)
    print('Você jogou {} o computador jogou {} o total de {}'.format(v, c, to),end='')
    print(' é PAR' if to%2==0 else ' é IMPAR')
    print('--' * 15)

    if ip=='par':
        if to%2==0:
            print('Você VENCEU')
            print('--'*15)

            cont+=1
        else:
            print('Você PERDEU')
            print('--'*15)
            break
    if ip=='impar':
        if to%2==1:
            print('Você VENCEU')
            print('--'*15)

            cont+=1
        else:
            print('Você PERDEU')
            print('--'*15)
            break



print(f'GAME OVER! você venceu {cont} a soma deu {to}')




