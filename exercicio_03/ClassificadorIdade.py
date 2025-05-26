# Classificador de Idade
# Objetivo: Criar um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:

# Criança (0-12 anos),
# Adolescente (13-17 anos),
# Adulto (18-59 anos) ou
# Idoso (60 anos ou mais).

idade = int(input("Por favor,digite sua idade: "))

if(idade > 0 and idade <= 12):
  print("Criança")

elif(idade < 17):
  print("Adolescente")

elif(idade < 59):
  print("Adulto")

else:
  print("Idoso")
