import requests

def site(site):

    try:
        requests.get(site)
    except:
        print(f'Site {site} NÃO ESTA ACESSÍVEL')
    else:
        print(f'O Site {site} ESTA ACESSÍVEL')

site('http://www.twitter.com.br')