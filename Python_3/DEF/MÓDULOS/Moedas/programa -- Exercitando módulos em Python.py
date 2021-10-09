import calculo as cal
pre=float(input('Digite um preço: R$'))
print(f'A metade de R${pre} é {cal.metade(p):.2f}')
print(f'O dobro de R${pre} é {cal.dob(p):.2f}')
print(f'Aumentando 10%, temos {cal.porc(p,10):.2f}')