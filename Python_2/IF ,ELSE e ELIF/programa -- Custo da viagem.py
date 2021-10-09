km=float(input('qual é a distacia da viagem(Km/h)? '))
print('Em uma viagem de {}Km'.format(km))
passagem=km*0.50
passagem2=km*0.45
if km <=200:
    print('O preço da sua passagem será de R${:.2f} '.format(passagem))
elif km >=200:
    print('O preço da sua passagem será de R${:.2f} '.format(passagem2))
# km*0.50 if distancia <= 200 else distancia*0.45

