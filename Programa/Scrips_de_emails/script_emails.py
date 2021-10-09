import re
import requests

req=requests.get('https://zecoxinha.com.br/')

padrão=re.findall(r'[\w*\.\*1234567890]+@+[\w*\!=\+\.@#$%¨&\*]+\.+\w+', req.text)

if padrão:
    print(padrão)
else:
    print('email invalido')