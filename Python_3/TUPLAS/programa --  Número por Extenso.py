num=('zero', 'um', 'dois','três','quatro','cinco','seis','sete','oito',
     'nove','dez','onze','doze','treze','quatorze','quize',
     'dezeseis','dezesete','dezoito','dezenove','vinte')

n=int(input('Digite um número de 0 a 20: '))
while n not in range(0,21):
    n=int(input('número incorreto!!\nDigite um número de 0 a 20: '))
for p,e in enumerate(num):
    if p==n:
        print(f'Por extenso esse número é {e}')
