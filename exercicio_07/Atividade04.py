import json

pessoa = {
    "nome": "Tayluan",
    "idade": 27,
    "cidade": "Rio de Janeiro"
}

arquivo_json = "pessoa.json"

with open(arquivo_json, "w", encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

with open(arquivo_json, "r", encoding='utf-8') as arquivo:
    dados_lidos = json.load(arquivo)

print(f"Nome: {dados_lidos['nome']}")
print(f"Idade: {dados_lidos['idade']}")
print(f"Cidade: {dados_lidos['cidade']}")

arquivo.close()
