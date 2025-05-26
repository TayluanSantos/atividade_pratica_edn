# Calculadora de IMC
# Objetivo: Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

peso = float(input("Por favor,digite o seu peso: "))
altura = float(input("Por favor,digite sua altura: "))

imc = peso / (altura * altura)

if(imc < 18.5):
  print(f"IMC do paciente: {imc:.2f} / Classificação: Baixo Peso")
elif(imc < 25):
  print(f"IMC do paciente: {imc:.2f} / Classificação: Peso Normal")
elif(imc < 30):
  print(f"IMC do paciente: {imc:.2f} / Classificação: Sobrepeso")
else:
   print(f"IMC do paciente: {imc:.2f} / Classificação: Obeso")