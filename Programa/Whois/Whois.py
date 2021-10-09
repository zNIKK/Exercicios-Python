import sys
import requests
print(f'\033[0;31m{"WHOIS":^30}\033[m')
s=input('Site: ')
try:
    r=requests.get('http://www.'+s)
    t=r.text

except:
    print('\033[0;31mDEU ALGO DE ERRADO. Tente novamente')
    s = input('Site: ')


