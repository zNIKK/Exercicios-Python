from veiculo import Veiculo
from Carro import carro

caminhão_rosa=Veiculo('rosa',6,'ford',10)

print(caminhão_rosa)

print('CAMINHÃO ROSA---''cor:',caminhão_rosa.cor,'//','rodas:',caminhão_rosa.rodas,'//','marca:',caminhão_rosa.marca,'//','tanque:',caminhão_rosa.tanque,'LITROS','//')

carro_azul=carro('azul','bmw',30)

print('====carro_azul====')
print('cor:',carro_azul.cor)
print('rodas:',carro_azul.rodas)
print('marca:',carro_azul.marca)
print('tanque:',carro_azul.tanque)
print('======================')
carro_azul.abastecer(10)
print('tanque:',carro_azul.tanque)
carro_azul.abastecer(70)
print('======================')
print('cor:',carro_azul.cor)
print('rodas:',carro_azul.rodas)
print('marca:',carro_azul.marca)
print('tanque:',carro_azul.tanque)



