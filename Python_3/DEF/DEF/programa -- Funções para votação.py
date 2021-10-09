ano = int(input('Em que ano você nasceu? '))
def votar(ano):
    from datetime import datetime
    anos=-ano+datetime.now().year
    if anos<=16:
        return f'Com {anos} anos: NÃO VOTA'
    elif 16<anos<18 or anos>70:
        return f'Com {anos} anos: VOTO OPCIONAL'
    else:
        return f'Com {anos} anos: VOTO OBRIGATORIO'

print(votar(ano))