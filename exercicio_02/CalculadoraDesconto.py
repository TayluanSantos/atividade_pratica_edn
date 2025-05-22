#Calculadora de Desconto
# Objetivo: Desenvolver um programa que calcula o desconto em uma loja


nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Nome do produto: {nome_produto}")
print(f"Preco Original: R${preco_original:.2f}")
print(f"Porcentagem de Desconto: {porcentagem_desconto}%")
print(f"Preco final: R${preco_final:.2f}")
print(f"Valor economizado: R${valor_desconto:.2f}")
