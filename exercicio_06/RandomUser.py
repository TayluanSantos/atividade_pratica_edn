import requests

response = requests.get('https://randomuser.me/api/')

try:
    dados = response.json()
    usuario = dados['results'][0]

    nome = (usuario["name"]["first"])
    sobrenome = (usuario["name"]["last"])
    pais = (usuario["location"]["country"])
    email = (usuario["email"])

    print(f"Nome: {nome} {sobrenome}")
    print(f"País: {pais}")
    print(f"Nome: {email}")

except Exception :
    print("Erro ao gerar usuário aleatório.")


