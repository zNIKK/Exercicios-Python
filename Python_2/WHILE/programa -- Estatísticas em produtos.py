print('--'*15)
print('LOJINHA')
print('--'*15)
pro=caro=barato=menor=cont=0
nome=None
while True:
    n=input('Nome do produto: ')
    pre=int(input('Preço: R$ '))
    c=' '
    pro+=pre
    cont+=1
    while c not in 'SsNn':
        c=str(input('Quer Continuar? [S/N]: '))
    if cont==1:
        menor=pre
        nome=n
    else:
        if pre<menor:
            menor=pre
            nome=n
    if pre>=1000:
        caro+=1
    elif pre<1000:
        barato+=1
    if c=='n':
        break
print('O total da compra foi de R${:.2f}\ntemos produto {} muito caro e {} mais barato\n'
      'O produto mais barato foi {} custando R${:.2f}'.format(pro,caro,barato,nome,menor))

