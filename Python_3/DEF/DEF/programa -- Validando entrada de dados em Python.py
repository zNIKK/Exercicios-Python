def leiaint(num):
    n=input('Digite um número: ')
    while not n.isnumeric():
        print('\033[0;31mERRO! Digite um número inteiro VÁLIDO!\033[m')
        n = input('Digite um número: ')
    return n


n=leiaint('Digite um número: ')
print(f'Você acabou de digitar um número {n}')
