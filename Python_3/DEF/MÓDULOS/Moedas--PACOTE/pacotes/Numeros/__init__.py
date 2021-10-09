from pacotes import Strings

def metade(n=0,formato=False):
    res=n/2
    return res if formato is False else Strings.moeda(res)


def dob(n=0,formato=False):
    res=n*2
    return res if formato is False else Strings.moeda(res)


def porc(n=0,taxa=0,formato=False):
    res=n+(n*taxa/100)
    return res if formato is False else Strings.moeda(res)

def dim(n=0,taxa=0,formato=False):
    res=n-(n*taxa/100)
    return res if formato is False else Strings.moeda(res)
