from time import sleep
print('-=' * 15)
def cont(c,f,p):
    print(f'contagem de {c} a {f} em {p}: ')
    for n in range(c,f+1,p):
        print(n,end=' ')
        sleep(0.3)
    print('FIM!')
    print('-='*15)
cont(0,10,1)
cont(10,0,-2)
print('Agora é a sua vez de personalizar a contagem:')
ini=int(input('Início: '))
fim=int(input('Fim: '))
pas=int(input('Passo: '))
if pas==0:
    pas=1
    if ini>fim:
        cont(ini,fim,-pas)

    else:
        cont(ini,fim,pas)
elif pas<0:
    pas*=-1
    if ini>fim:
        cont(ini,fim,-pas)

    else:
        cont(ini,fim,pas)
else:
    if ini > fim:
        cont(ini, fim, -pas)

    else:
        cont(ini, fim, pas)