import math
from os import system
while True:
    int=int(input('Digite um ângulo:'))
    ang=math.radians(int)
    sen=math.sin(ang)
    cos=math.cos(ang)
    tan=math.tan(ang)

    print('{}° tem o SENO de {:.2f}\n{}° tem o COSSENO de {:.2f}\n{}° tem a TANGENTE de {:.2}'.format(int,sen,int,cos,int,tan))
    c=input('Quer continuar?[S/N]: ').upper()
    while c not in 'SN':
        c=input('Quer continuar?[S/N]: ').upper()
    if c=='N':
        break
    else:
        system('cls')
        
