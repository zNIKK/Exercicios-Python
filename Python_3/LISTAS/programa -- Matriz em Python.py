list=[[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for i in range(0,3):
        list[l][i]=(int(input(f'Digite um valor para [{l},{i}]: ')))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{list[l][c]}]',end=' ')
    print()