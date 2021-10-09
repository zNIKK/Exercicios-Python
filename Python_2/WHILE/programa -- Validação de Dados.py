sex = input('Informe seu sexo [M/F]:')
while sex not in'mf':
    sex=input('Sexo Invalido! Digite [M(masculino)/F(Femenino)]:')

print('Sexo {} registrado com sucesso!!'.format(sex.upper()))


