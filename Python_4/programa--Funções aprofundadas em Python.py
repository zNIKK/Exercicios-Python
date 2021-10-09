while True:
    def leiaint(txt):
        while True:
            try:
                n=int(input(txt))
                return n
            except:
                print('\033[0;31mERRO! Digite um número inteiro VÁLIDO!\033[m')
    def leiareal(txt):
        while True:
            try:
                n=float(input(txt))
                return n
            except:
                print('\033[0;31mERRO! Digite um número real VÁLIDO!\033[m')

    no=leiaint('Digite um número inteiro: ')
    no1=leiareal('Digite um número real: ')
    print(f'Você acabou de digitar um número inteiro: {no}\n'
          f'E um número real {no1}')
