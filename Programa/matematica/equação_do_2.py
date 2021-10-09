
while True:
    import random
    import os
    while True:
        print('=='*15)
        print('Equação do 1° grau || Treino')
        print('=='*15)
        # numeros randomicos
        a = random.randint(1,15)
        b = random.randint(1,64)
        x = random.randint(1,18)
        # formula: [ax + b = c]
        t = a * x + b
        print(f'>> {a}x + {b} = {t}')

        # tratamento de erros
        try:
            res=int(input('Qual é o valor do x?: '))

        except ValueError:
            print('caractere inválido! Tente novamente.')
            input('pressione a tecla ENTER para continuar...')
            break

        except Exception as err:
            print(f'detectamos o seguinte erro:\n{err}')
            input('pressione a tecla ENTER para continuar...')
            break

        # identificar se sua resposta está certa ou errada
        if res == int(x):
            print(f'Correto!!! o x é igual a {x}')
            input('pressione a tecla ENTER para continuar...')

            os.system('cls')

        else:
            print(f'Errou!!! o x é igual a {x}')
            input('pressione a tecla ENTER para continuar...')

            os.system('cls')

