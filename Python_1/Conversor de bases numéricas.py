
num=int(input('digite um número inteiro: '))

print('escolha as bases de conversão:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
op=int(input('Escolha:'))

if op==1:
    print('{} convertido para BINÁRIO: {}'.format(num,bin(num)[2:]))
elif op==2:
    print('{} convertido para OCTAL: {}'.format(num,oct(num)[2:]))
elif op==3:
    print('{} convertido para HEXADECIMAL: {}'.format(num,hex(num)[2:]))