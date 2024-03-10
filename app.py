import os
import requests
import json

from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome = item['Company']
        if nome not in dados_restaurante:
            dados_restaurante[nome] = []
        
        dados_restaurante[nome].append({

            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })

else:
    print(f'erro {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
