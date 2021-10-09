dict = {}
def notas(*num,sit=False):
    """—> função para analizar notas em situações de varios.
    :param num: uma ou mais notas dos alunos.
    :param sit: Valor opcional, indicando se deve ou não adcionar a situação da sua nota.
    :return: O dicionário com várias informações sobre o aluno.
"""
    t=0
    mai=0
    cont=0
    for n in num:
        t+=n
        dict['total']=t
        cont+=1
        if cont==1:
            mai=n
        else:
            if n>mai:
                dict['maior']=n
            else:
                dict['menor']=n
    dict['média']=dict['total']/cont
    if sit==True:
        if dict['média']<=5:
            dict['situação']='RUIM'
        elif 5<dict['média']<7:
            dict['situação']='RAZOÁVEL'
        else:
            dict['situação']='BOA'

    return dict

print(notas(5.5,9.5,10,1.1,sit=True))
