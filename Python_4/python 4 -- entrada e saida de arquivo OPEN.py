import os
diretorio=input('qual será o nome do "arquivo"?:')
nome=input('para onde esse "arquivo" vai?:')
inco=nome+diretorio
arquivo=inco +'.txt'
try:
    open(arquivo, 'x')
except:
    os.remove(arquivo)
while True:
    print('----------------------')
    print('pressione E para escrever?\npressione L para ler?')
    print('----------------------')
    str=input('o que deseja?:')
    print('----------------------')

    if str=='E':
        escrever=input('escreva:')
        op=open(arquivo, 'w')
        op.write(escrever)
        print('=== mensagem guardada ===')
        per=input('deseja acrescentar algo?:')
        while per=='sim':
            inp = input('escreva:')
            op=open(arquivo, 'a')
            op.write(escrever)
            per=input('deseja acrescentar algo?:')
    elif str=='L':
        op=open(arquivo, 'r')
        print(op.read())