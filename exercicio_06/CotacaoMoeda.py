#Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).

import requests

def calcular_cotacao(moedas_conversao):

    moedas_conversao = moedas_conversao.upper()
    moeda_formatado = moedas_conversao.replace("-","")

    url = f"https://economia.awesomeapi.com.br/json/last/{moedas_conversao}"

    try:
        response = requests.get(url).json()

        print(f"Moedas de conversão:{moedas_conversao}")
        print(f"Valor mínimo da cotação: R$ {float(response[moeda_formatado]['low']):.2f}")
        print(f"Valor máximo da cotação: R$ {float(response[moeda_formatado]['high']):.2f}")
        print(f"Última atualização: {(response[moeda_formatado]['create_date'])}")


    except Exception:
          print("Erro ao fazer requisição")

    
calcular_cotacao("USDBRL")

