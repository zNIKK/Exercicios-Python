n=0
cont=0
t = int(input('Digite um valor para a tabuada: '))
print('~~'*10)
while True:
    n += t
    cont+=1
    print('{} x {} = {}'.format(t,cont,n))
    if cont==10:
        n=t=cont=0
        print('~~'*10)
        t = int(input('Digite um valor para a tabuada: '))
        print('~~'*10)
    if t<=0:
        break
print('programa ENCERRADO COM SUCESSO! Volte sempre!')
print('~~' * 10)









