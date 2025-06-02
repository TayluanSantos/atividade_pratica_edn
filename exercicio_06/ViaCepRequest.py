# Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
# utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

import requests

def consultar_cep(cep, formato_resposta):

    url= "https://viacep.com.br/ws"

    if cep.isdigit() and len(cep) == 8:
        try:
            response = requests.get(f"{url}/{cep}/{formato_resposta}/")
            dados = response.json()

            print("Logradouro: ", dados["logradouro"])
            print("Bairro: ", dados["bairro"])
            print("Cidade: ", dados["localidade"])

        except Exception:
            print("Erro ao consultar o CEP.")
    else:
        print("CEP inválido. Deve conter exatamente 8 dígitos numéricos.")

consultar_cep("25555241","json")
