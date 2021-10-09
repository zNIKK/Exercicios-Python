from datetime import datetime

dict={}
list=[]
dict['nome']=input('Nome: ')
dict['ano']=int(input('Ano de Nascimento: '))
dict['trabalho']=int(input('Carteira de trabalho (0 não tem ): '))
if dict['trabalho']>0:
    dict['contratação']=int(input('Ano de contratação: '))
    dict['salário']=int(input('Salário R$'))
    aposentadoria=-(-dict['ano']+2018)+70
dict['ano']=-dict['ano']+datetime.now().year
list.append(dict.copy())
print('-='*30)
for e in list:
    for k,v in e.items():
            print(f'- {k} tem o valor {v}')

if dict['trabalho']>0:
    print(f'- Aposentadoria tem o valor {aposentadoria}')


