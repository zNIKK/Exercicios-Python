print('=='*15)
print('{:^30}'.format('BANCO'))
print('=='*15)
v=int(input('Que valor você quer sacar? R$'))
to=v
c50=50
c20=20
c10=10
c1=1
cont=cont1=cont2=cont3=0
while True:
    if not to == 0:
        if to>=c50:
            to -= c50
            cont+=1
        else:
            if to<=c50:
                if to>=c20:
                    to-=c20
                    cont1+=1
                else:
                    if to<=c20:
                        if to>=c10:
                            to -= c10
                            cont2 += 1
                        else:
                            if to<=c10:
                                if to>=c1:
                                    to -= c1
                                    cont3 += 1
    else:
        break
print('=='*15)
print(f'{cont} cédulas de R$50\n{cont1} cédulas de R$20\n{cont2} cédulas de R$10\n{cont3} cédulas de R$1')
print('=='*15)

