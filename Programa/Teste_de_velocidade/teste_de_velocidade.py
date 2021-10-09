import speedtest
while True:
    print('verificando a velocidade da sua internet...')
    s = speedtest.Speedtest()
    d = s.download()
    u = s.upload()
    us = float(u)/(1025*1025)
    server=[]
    s.get_servers(server)
    p = s.results.ping
    ds = float(d)/(1025*1025)
    print('=============== Teste de velocidade ===============')
    print(f'ping: {p:.0f}ms')
    print(f'donwload: {ds:.2f}Mbps')
    print(f'Upload: {us:.2f}Mbps')
    print('===================================================')
    c = input('Continuar a testar a sua internet?[S/N]: ').upper()
    while c not in 'SN':
        print('=== Digite apenas S ou N para continuar ===')
        c = input('Continuar a testar a sua internet?[S/N]: ').upper()
    if c=='N':
        break

