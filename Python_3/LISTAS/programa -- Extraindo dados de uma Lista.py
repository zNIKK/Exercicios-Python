list=[]
cont=0
while True:
    n=int(input('Digite um número: '))
    c=' '
    list.append(n)
    cont+=1
    while c not in 'SsNn':
        c=input('Quer continuar? [S/N]').upper()
    if c=='N':
        break
print('-='*30)
if 5 in list:
    cinco='O valor 5 faz parte da lista!'
else:
    cinco='O valor 5 não foi encontrado na lista'
list.sort(reverse=True)
print(f'Você digitou {cont} elementos\nOs valores em ordem decrescente são {list}')
print(cinco)

