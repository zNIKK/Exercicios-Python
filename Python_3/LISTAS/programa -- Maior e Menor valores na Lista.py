list=[]
maior=0
menor=0
p=p1=0
for n in range(0,5):
    num=int(input(f'Digite um valor na posição {n}: '))
    list.append(num)
    if n==0:
        maior=num
        menor=num
        p=n
        p1=n
    else:
        if maior>num:
            maior=num
            p=n
        if menor<num:
            menor=num
            p1=n
print('-='*30)
print(f'Você digitou os valores {list}')
print(f'O maior valor digitado foi {menor} nas posições: ',end='')
for i,v in enumerate(list):
    if v==menor:
        print(f'{i}',end=' ')

print(f'\nO menor valor digitado foi {maior} nas posições: ',end='')
for i, v in enumerate(list):
    if v==maior:
        print(f'{i}',end=' ')
print('')
print('-='*30)



