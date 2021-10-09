def fat(num=1):
    f=1
    for c in range(num,0, -1):
        f*=c
    return f

f1=fat(4)
f2=fat(6)
f3=fat(2)
print(f'Os resultados são {f1}, {f2} e {f3}')