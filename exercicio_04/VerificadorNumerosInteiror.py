# Regras:
# Continuar pedindo números até que o usuário digite 'fim'.
# Informar se o número é par ou ímpar.
# Se não for um número inteiro, informar o erro e continuar.
# Ao final, mostrar a quantidade total de números pares e ímpares inseridos.

numeros_pares = []
numeros_impares = []

while True:
    
  entrada = input("Digite um numero inteiro(ou 'fim' para encerrar): ").strip().lower()

  if entrada == "fim":
    break

  try:
    numero_inteiro = int(entrada)
    if (numero_inteiro % 2 == 0 ):
      numeros_pares.append(numero_inteiro)
    elif (numero_inteiro % 2 != 0):
      numeros_impares.append(numero_inteiro)
  except ValueError:
    print("Entrada inválida.Por favor,digite um numero inteiro!")

      
print("Quantidade numeros pares:",len(numeros_pares))
print("Quantidade numeros impares:",len(numeros_impares))