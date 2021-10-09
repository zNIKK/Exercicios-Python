from cliente import Cliente
from Conta import Conta
print('=======Cadastro=======')
nome=input('Nome:')
email=input('Email:')
senha=input('senha:')
print('=========Login=========')
nome1=input('nome:')
senha1=input('senha:')
if nome == nome1 and senha == senha1:
    consumidor = Cliente(nome, email, senha)

    print('============CONTA BANCÁRIA============')
    print('Seu nome é:', consumidor.nome)
    print('seu email é:', consumidor.email)
    print('sua senha é:', consumidor.senha)
    print('================SALDO=================')

    dinheiro = Conta(2500)
    print('saldo:', dinheiro.saldo)
    opção = input('deseja sacar,depositar ou sair da conta?')

    if opção == 'sacar':
        valor = int(input('sacar quanto?:'))
        dinheiro.sacar(valor)
        print('saldo:', dinheiro.saldo)

    elif opção == 'depositar':
        valor2 = int(input('depositar quanto?:'))
        dinheiro.depositar(valor2)
        print('saldo:', dinheiro.saldo)

    elif opção == 'sair da conta':
        print('=======Cadastro=======')
        nome = input('Nome:')
        email = input('Email:')
        senha = input('senha:')
        print('=========Login=========')
        nome1 = input('nome:')
        senha1 = input('senha:')
        if nome == nome1 and senha == senha1:
            consumidor = Cliente(nome, email, senha)

            print('============CONTA BANCÁRIA============')
            print('Seu nome é:', consumidor.nome)
            print('seu email é:', consumidor.email)
            print('sua senha é:', consumidor.senha)
            print('================SALDO=================')

            dinheiro = Conta(2500)
            print('saldo:', dinheiro.saldo)
            opção = input('deseja sacar,depositar ou sair da conta?')

            if opção == 'sacar':
                valor = int(input('sacar quanto?:'))
                dinheiro.sacar(valor)
                print('saldo:', dinheiro.saldo)

            elif opção == 'depositar':
                valor2 = int(input('depositar quanto?:'))
                dinheiro.depositar(valor2)
                print('saldo:', dinheiro.saldo)

    else:
        print(dinheiro.saldo)

else:
    print('login incorreto')














