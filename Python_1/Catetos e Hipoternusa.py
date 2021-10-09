import math

cateto_oposto=float(input('comprimento do cateto oposto:'))
cateto_adjacente=float(input('comprimento do cateto adjacente:'))

conta=cateto_oposto+cateto_adjacente
conta2=(conta**2)
hipotenusa=math.sqrt(conta2)


print('A sua hiportenusa é de {:.2f}'.format(hipotenusa))