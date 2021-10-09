import math
int=int(input('Digite um ângulo:'))
ang=math.radians(int)
sen=math.sin(ang)
cos=math.cos(ang)
tan=math.tan(ang)

print('{}° tem o SENO de {:.2f}\n{}° tem o COSSENO de {:.2f}\n{}° tem a TANGENTE de {:.2}'.format(int,sen,int,cos,int,tan))