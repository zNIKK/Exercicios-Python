list=[[],[]]
for n in range(1,8):
    num=int(input(f'Digite o {n}° valor: '))
    if num%2==0:
        list[0].append(num)
    else:
        list[1].append(num)
print('-='*15)
print(f'Os valores PARES digitados foram {list[0]}')
print(f'Os valores IMPARES digitados foram {list[1]}')