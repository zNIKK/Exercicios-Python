from veiculo import Veiculo
class carro(Veiculo):

    def __init__(self,cor,marca,tanque):
        Veiculo.__init__(self,cor,4,marca,tanque)

    def abastecer(self,litros):
        print('abastecendo...')
        if self.tanque + litros > 50:
            print('!!tanque cheio!!')
        else:
            self.tanque += litros