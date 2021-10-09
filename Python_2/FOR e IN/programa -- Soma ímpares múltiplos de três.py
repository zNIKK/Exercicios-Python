s=0
c=0
for i in range(0,501,3):
    if i % 2 == 1:
        s+=i
        c+=1
print('A soma de todos os {} valores solicitados é {}'.format(c,s))