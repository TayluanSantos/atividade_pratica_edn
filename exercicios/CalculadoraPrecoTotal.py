#Simule o cálculo do preço total de um produto. Defina o nome do produto, o preço unitário e a quantidade comprada. Em seguida, calcule e exiba:

def calcular_preco_total_produto(nome_produto,preco_unitario,quantidade):

    preco_total = preco_unitario * quantidade

    print(f"Produto: {nome_produto}")
    print(f"Valor Unitario: {preco_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço Total: {preco_total:.2f}")


calcular_preco_total_produto ("Café",35,2)
