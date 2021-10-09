porcen=float(input('R$:'))

dindin=float(input('%'))

calcu=(porcen/100)*dindin
total=dindin-calcu

print('o dinheiro que era de R${} agora com {:.1f}% de desconto, agora passa a ser R${:.2f}'.format(dindin,porcen,total))