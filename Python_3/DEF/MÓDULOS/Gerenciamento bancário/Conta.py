class Conta:

    def __init__(self, saldo):
        self.saldo=saldo
        self.depositar

    def sacar(self,dinheiro):
        if self.saldo - dinheiro < 2000:
            print('!!limite excedido!!')
        else:
            self.saldo-=dinheiro

    def depositar(self,dinheiro):
        self.saldo+=dinheiro
        print('!!depositado com sucesso!!')













