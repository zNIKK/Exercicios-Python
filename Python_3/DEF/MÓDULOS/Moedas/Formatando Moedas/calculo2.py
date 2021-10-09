def metade(n=0,formato=False):
    res=n/2
    return res if formato is False else moeda(res)


def dob(n=0,formato=False):
    res=n*2
    return res if formato is False else moeda(res)


def porc(n=0,taxa=0,formato=False):
    res=n+(n*taxa/100)
    return res if formato is False else moeda(res)


def moeda(n=0,m='R$'):
    return f'{m}{n:.2f}'.replace('.',',')

def dim(n=0,taxa=0,formato=False):
    res=n-(n*taxa/100)
    return res if formato is False else moeda(res)

def resumo(n=0,p1=10,p2=10,formato=False):
    if formato==True:
        print('——'*15)
        print(f'{"RESUMO DO VALOR":^30}')
        print('——'*15)

        print(f'Preço analizado: \tR${moeda(n):>3}')
        print(f'Dobro do preço: \tR${dob(n,True):>3}')
        print(f'Metade do preço: \tR${metade(n,True):>3}')
        print(f'{p1}% de Aumento: \t\tR${porc(n, p1, True)}' if len(str(p1))==1 else f'{p1}% de Redução: \tR${dim(n, p1, True)}')
        print(f'{p2}% de Redução: \t\tR${dim(n, p2, True)}' if len(str(p2))==1 else f'{p2}% de Redução: \tR${dim(n, p2, True)}')
        print('——'*15)
    else:
        print('——' * 15)
        print(f'{"RESUMO DO VALOR":^30}')
        print('——' * 15)

        print(f'Preço analizado: \tR${n}')
        print(f'Dobro do preço: \tR${dob(n)}')
        print(f'Metade do preço: \tR${metade(n)}')
        print(f'{p1}% de Aumento: \tR${porc(n, p1)}' if len(str(p1))==1 else f'{p1}% de Redução: \tR${dim(n, p1)}')
        print(f'{p2}% de Redução: \t\tR${dim(n, p2)}' if len(str(p2))==1 else f'{p2}% de Redução: \tR${dim(n, p2)}')


        print('——' * 15)

