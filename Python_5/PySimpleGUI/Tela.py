import PySimpleGUI as sg
import requests as rq
import json

req=None

try:
    req = rq.get('https://economia.awesomeapi.com.br/json/all')
except:
    print('Erro na requisição')
    exit()

dicionario = json.loads(req.text)
class telapython:

    sg.theme('DarkAmber')
    def __init__(self):
        s = float(dicionario["USD"]["high"]) + float(dicionario["USD"]["low"])
        m = s / 2
        layout = [
            [sg.Text(f'Nome: {dicionario["USD"]["codein"]}')],
            [sg.Text(f'Tipo: {dicionario["USD"]["name"]}')],
            [sg.Text(f'{dicionario["USD"]["create_date"]}')],
            [sg.Text(f'R$ {m:.2f}',size=(30,0))],
            [sg.Button(f'{dicionario["EUR"]["name"]}',key='EUR')],
            [sg.Button(f'{dicionario["BTC"]["name"]}',key='BTC')],
        ]
        janela=sg.Window('Cotação').layout(layout)
        self.button, self.values = janela.Read()
    def BRL(self):
        print(self.values)

Tela = telapython()
Tela.BRL()
