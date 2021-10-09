print('=='*30)
print('{:^57}'.format('LISTAGEM DE PREÇOS'))
print('=='*30)
listagem=('lapis',1.75,
          'Borracha',2.00,
          'Caderno',15.00,
          'Estojo',25.00,
          'Transferidor',4.20,
          'Compasso',9.99)

for n in range(0, len(listagem)):
    if n%2==0:
        print(f'{listagem[n]:.<30}',end='')
    if n%2==1:
        print(f'R${listagem[n]:>5.2f}')
print('=='*30)

