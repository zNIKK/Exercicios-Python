casa=int(input('Valor da casa: R$'))
salario=int(input('qual o seu salário: R$'))
anos=int(input('Quantos anos de financiamento:'))
prestacao=casa/(anos*12)
minimo=salario*30/100
print('para pagar a casa de R${} em {} anos a prestação será de R${:.2f}'.format(casa,anos,prestacao))

if prestacao <= minimo:
    print('\033[0;32mEmpréstimo CONCEDIDO!')
else:
    print('\033[0;31mEmpréstimo NEGADO!')



