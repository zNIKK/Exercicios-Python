vel=float(input('Qual a velocidade atual do carro? '))

if vel <= 80:
    print('Tenha um bom dia! dirija com segurança!')
elif vel > 80:
    multa=(-80+vel)*7
    print('MULTADO! Você exedeu o limite permitido que é de 80Km/h\n'
          'A MULTA será de R${:.2f}'.format(multa))

