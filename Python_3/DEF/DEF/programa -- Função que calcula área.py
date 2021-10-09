def area(l,c):
    a=l*c
    print(f'A área de um terreno {l} * {c} é de {a}m².')
print('▬' * 25)
print('CONTROLE DE TERRENO')
print('▬'*25)
l=float(input('LARGURA (m): '))
c=float(input('COMPRIMENTO (m): '))
print('▬'*25)
area(l,c)
input('Pressione ENTER para fechar')