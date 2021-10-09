import time
def abre():
    try:
        arquivo = open('arquivo.txt')
        return arquivo
    except Exception as error:
        print('aconteceu um erro', error)
        return False

while not abre():
    print('tentando abrir...')
    time=time.sleep(9)
    open('arquivo.txt', 'w')
print('encontrei o arquivo')
print('abrindo o arquivo...')
open('arquivo.txt', 'r')
