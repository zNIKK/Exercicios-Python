s=0
c=0
for n in range(6):
    num=int(input('digite o {}º número:'.format(n+1)))
    if num%2==0:
        s+=num
        c+=1
print('a soma dos {} números pares é {}'.format(c,s))