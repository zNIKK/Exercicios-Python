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
class Eur:
    def __init__(self):
        s = float(dicionario["USD"]["high"]) + float(dicionario["USD"]["low"])
        m = s / 2
        layout = [
            [sg.Text(f'Nome: {dicionario["EUR"]["codein"]}')],
            [sg.Text(f'Tipo: {dicionario["EUR"]["name"]}')],
            [sg.Text(f'{dicionario["EUR"]["create_date"]}')],
            [sg.Text(f'R$ {m:.2f}', size=(30, 0))],
            [sg.Button(f'{dicionario["USD"]["name"]}', key='USD')],
            [sg.Button(f'{dicionario["BTC"]["name"]}', key='BTC')],
        ]
        janela = sg.Window('Cotação').layout(layout)
        self.button, self.values = janela.Read()
    def iniciar(self):
        print(self.values)

Tela=Eur()
Tela.iniciar()
