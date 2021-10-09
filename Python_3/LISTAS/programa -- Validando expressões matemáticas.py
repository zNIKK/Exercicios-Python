e=input('Digite uma expressão matemática: ')
ap=e.count('(')
fp=e.count(')')
if ap == fp:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está invalida!')