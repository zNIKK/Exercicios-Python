from time import sleep
def maior(*num):
    print('-='*25)
    print('Analizando valores passados...')
    for i in num:
        print(i,end=' ')
        sleep(0.3)
    print(f'foram informados ao todo {len(num)} valores')
    m=0
    c=-1
    while c<len(num)-1:
        c+=1
        if num[c]>m:
            m=num[c]
    print(f'o maior valor informado foi {m}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
print('-=' * 25)
