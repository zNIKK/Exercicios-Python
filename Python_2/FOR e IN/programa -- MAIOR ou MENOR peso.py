maior=0
menor=0
for i in range(1,6):
    peso=float(input('{}ª Valor: '.format(i)))
    if i==1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso
print('O maior valor lido foi de {}Kg'.format(maior))
print('O menor valor lido foi de {}Kg'.format(menor))