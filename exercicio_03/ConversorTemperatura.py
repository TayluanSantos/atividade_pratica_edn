# Conversor de Temperatura
# Objetivo: Criar um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

valor_temperatura = float(input("Digite o valor da temperatura: "))
unidade_origem = str.lower(input("Digite a unidade de origem (Celsius, Fahrenheit ou Kelvin): "))
unidade_conversao = str.lower(input("Digite a unidade de conversão (Celsius, Fahrenheit ou Kelvin): "))

# Celsius -> Fahrenheit
if unidade_origem == "celsius" and unidade_conversao == "fahrenheit":
    resultado_conversao = (valor_temperatura * 1.8) + 32
    print(f"A temperatura de {valor_temperatura} graus Celsius corresponde a {resultado_conversao:.1f} graus Fahrenheit.")

# Celsius -> Kelvin
if unidade_origem == "celsius" and unidade_conversao == "kelvin":
    resultado_conversao = valor_temperatura + 273.15
    print(f"A temperatura de {valor_temperatura} graus Celsius corresponde a {resultado_conversao:.1f} graus Kelvin.")

# Kelvin -> Celsius
if unidade_origem == "kelvin" and unidade_conversao == "celsius":
    resultado_conversao = valor_temperatura - 273.15
    print(f"A temperatura de {valor_temperatura} graus Kelvin corresponde a {resultado_conversao:.1f} graus Celsius.")

# Kelvin -> Fahrenheit
if unidade_origem == "kelvin" and unidade_conversao == "fahrenheit":
    resultado_conversao = ((valor_temperatura - 273.15) * 1.8) + 32
    print(f"A temperatura de {valor_temperatura} graus Kelvin corresponde a {resultado_conversao:.1f} graus Fahrenheit.")

# Fahrenheit -> Celsius
if unidade_origem == "fahrenheit" and unidade_conversao == "celsius":
    resultado_conversao = (valor_temperatura - 32) / 1.8
    print(f"A temperatura de {valor_temperatura} graus Fahrenheit corresponde a {resultado_conversao:.1f} graus Celsius.")

# Fahrenheit -> Kelvin
if unidade_origem == "fahrenheit" and unidade_conversao == "kelvin":
    resultado_conversao = (valor_temperatura - 32) * 5/9 + 273.15
    print(f"A temperatura de {valor_temperatura} graus Fahrenheit corresponde a {resultado_conversao:.1f} graus Kelvin.")
