r='S'
cont=0
s=0
maior=0
menor=0
while r!='N':
    n=int(input('Digite um número: '))
    r=input('Quer continuar [S/N]: ').upper()
    s+=n
    cont+=1
    s/=cont
    if cont==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n




print('Você digitou {} números e a média foi de {}\nO MAIOR valor foi de {} e o MENOR foi de {}'.format(cont,s,maior,menor))