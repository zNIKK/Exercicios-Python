tupla=('aprender','python','programar','linguagem','estudar','programador')
print('-='*15)
for p in tupla:
    print(f'\nNa palavra {p} temos:',end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra,end=' ')