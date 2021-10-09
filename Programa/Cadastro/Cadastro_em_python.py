import menu
import os

try:
    ar=open('G:\python\Programas.py\Programa\Pessoas_cadastradas.txt', 'x')
    print()
except:
    ar=open('G:\python\Programas.py\Programa\Pessoas_cadastradas.txt', 'a')

while True:
    menu.linha(f'{"MENU PRINCIPAL":^45}')
    print('\033[0;33m1 — Ver pessoas cadastradas')
    print('2 — Cadastrar nova Pessoa')
    print('3 — Excluir uma conta')
    print('4 — Sair do Sistema\033[m')
    print('\033[0;35m—'*50)
    while True:
        try:
            op=int(input('Sua opção: '))
            break
        except Exception as err:
            print(f'\033[0;30mERRO DO TIPO:\033[0;31m {err}\033[m')
    while op>3 or op<0:
        print('\033[0;31mErro opção invalida. Por favor digite um número que esteja na lista')
        op=int(input('Sua opção: '))
    if op==1:
        print('\033[0;34m—'*50)
        print(f'PESSOAS CADASTRADAS')
        print('—'*50)
        ar = open('G:\python\Programas.py\Programa\Pessoas_cadastradas.txt', 'r')
        print(ar.read())
    elif op==2:
        print('\033[0;34m—'*50)
        print(f'{"CADASTRAR UMA NOVA PESSOA":^45}')
        print('—'*50)
        ar = open('G:\python\Programas.py\Programa\Pessoas_cadastradas.txt', 'a')

        n=input('Nome: ')
        ar.write(f'\033[0;33m{n:<15}')
        i=input('Idade: ')
        ar.write(f'{i:>15} anos')


    elif op==3:
        break
print('—' * 50)
print(f'{"Saindo do sistema... Até logo!":^45}')
print('—' * 50)
