#Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.​
# Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.​

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):

    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)

    print(f"Valor da conta: R${valor_conta:.2f}")
    print(f"Porcentagem da gorjeta: {porcentagem_gorjeta}%")
    print(f"Valor da gorjeta: R${valor_gorjeta:.2f}")

calcular_gorjeta(120,15)
