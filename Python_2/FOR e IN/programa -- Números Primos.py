num=int(input('Digite um número: '))
tot=0
for n in range(1,num+1):
    if num%n==0:
        print('\033[0;32m', end=' ')
        tot+=1
    else:
        print('\033[0;31m', end=' ')
    print(n, end=' ')

print('\n\033[mO número {} foi divisivel {} vezes'.format(num,tot))

if 2==tot:
    print('O número {} É PRIMO'.format(num))
else:
    print('O número {} NÃO É PRIMO'.format(num))
