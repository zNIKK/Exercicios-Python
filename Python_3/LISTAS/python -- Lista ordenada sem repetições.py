list=[]
for e in range(0,5):
    v=int(input('Digite um valor: '))
    list.append(v)
    list.sort()
    ind=list.index(v)
    if e==0:
        print('adcionado no final da lista...')
    elif ind==e:
        print('adcionado no final da lista...')
    else:
        print(f'Adcionado na posição {ind} da lista')
print('-='*15)
print(list)



#        print(f'Adcionado na posição {c} da lista')

#        print('adcionado no final da lista...')
