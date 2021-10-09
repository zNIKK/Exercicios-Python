from pacotes import Numeros

def erros(txt):
    v=False
    while not v:
        entrada=str(input(txt))
        if entrada.isalpha():
            if ',' in entrada:
                re = f'{entrada}'.replace(',', '.')
                return float(re)
            print(f'\033[0;31mERRO \"{entrada}\" é um preço invalido\033[m')

        else:
            v=True
            return float(entrada)

def moeda(n=0,m='R$'):
    return f'{m}{n:.2f}'.replace('.',',')


def resumo(n=0,p1=10,p2=10,formato=False):
    if formato==True:
        print('——'*15)
        print(f'{"RESUMO DO VALOR":^30}')
        print('——'*15)

        print(f'Preço analizado: \tR${moeda(n):>3}')
        print(f'Dobro do preço: \tR${Numeros.dob(n,True):>3}')
        print(f'Metade do preço: \tR${Numeros.metade(n,True):>3}')
        print(f'{p1}% de Aumento: \t\tR${Numeros.porc(n, p1, True)}' if len(str(p1))==1 else f'{p1}% de Redução: \tR${Numeros.dim(n, p1, True)}')
        print(f'{p2}% de Redução: \t\tR${Numeros.dim(n, p2, True)}' if len(str(p2))==1 else f'{p2}% de Redução: \tR${Numeros.dim(n, p2, True)}')
        print('——'*15)
    else:
        print('——' * 15)
        print(f'{"RESUMO DO VALOR":^30}')
        print('——' * 15)

        print(f'Preço analizado: \tR${n}')
        print(f'Dobro do preço: \tR${Numeros.dob(n)}')
        print(f'Metade do preço: \tR${Numeros.metade(n)}')
        print(f'{p1}% de Aumento: \tR${Numeros.porc(n, p1)}' if len(str(p1))==1 else f'{p1}% de Redução: \tR${Numeros.dim(n, p1)}')
        print(f'{p2}% de Redução: \t\tR${Numeros.dim(n, p2)}' if len(str(p2))==1 else f'{p2}% de Redução: \tR${Numeros.dim(n, p2)}')
        print('——' * 15)

