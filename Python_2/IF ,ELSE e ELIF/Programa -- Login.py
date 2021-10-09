nome=input('digite o seu nome?\n')
senhas=input('digite sua senha\n')

blibioteca={'usuario':nome,'senha':senhas}

usuario=input('usuario:')
password=input('senha:')

if password == usuario and password:
    print('login aceito')
else:
    print('login incorreto')