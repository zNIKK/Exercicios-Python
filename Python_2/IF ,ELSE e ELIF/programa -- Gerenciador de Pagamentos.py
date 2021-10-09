pre=float(input('Preço da compras: R$'))

print('--='*4,'FORMAS DE PAGAMENTO','=--'*4)
print('[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista no cartão\n[ 3 ] 2X ou mais no cartão')
op=input('Escolha:')

if op=='1':
    print('sua compra de \033[0;32mR${}\033[m vai custar \033[0;32mR${}\033[m no final'.format(pre,-0.1*pre+pre))
elif op=='2':
    print('sua compra de \033[0;32mR${}\033[m vai custar \033[0;32mR${}\033[m no final'.format(pre,-0.05*pre+pre))
elif op=='3':
    print('\033[0;31m2X\033[m no cartão\n'
          '\033[0;31m3X\033[m no cartão\n'
          '\033[0;31m4X\033[m no cartão\n'
          '\033[0;31m5X\033[m no cartão\n'
          '\033[0;31m6X\033[m no cartão\n'
          '\033[0;31m7X\033[m no cartão\n'
          '\033[0;31m8X\033[m no cartão\n'
          '\033[0;31m9X\033[m no cartão\n'
          '\033[0;31m10X\033[m no cartão\n'
          '\033[0;31m11X\033[m no cartão\n'
          '\033[0;31m12X\033[m no cartão')
    parc=int(input('Quantas parcelas?'))
    if parc==2:
        print('vai custar \033[0;33mR${}0\033[m no final'.format(pre))
    elif parc==3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12:
        print('sua compra de \033[0;32mR${}\033[m parcelada em {}x de \033[0;32mR${:.1f}0\033[m COM JUROS\n'
              'no final ficará \033[0;32m{}\033[m COM JUROS'.format(pre,parc,(0.2*pre+pre)/parc,0.2*pre+pre))
    else:
        print('!!! NÚMERO ERRADO !!!\n'
              'escolha um número de 2 a 12')
else:
    print('esse número não EXISTE na lista')