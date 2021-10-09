def fat(num,show=True):
    '''—> Calcular fatorial de um número.
    :param num: Número a ser calculado.
    :param show: (Opcional) Mostra ou não a conta.
    :return: O valor fatorial de um número.'''
    f=1
    for c in range(num,0,-1):
        if show==True:
            print(c,end='')
            print(' = ' if c==1 else ' x ',end='')
        else:
            f*=c
    return f

print(fat(6,show=False))