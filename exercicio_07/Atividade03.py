# Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import csv

with open ("atividade-02.csv","r",newline='') as csvfile:

    reader = csv.reader(csvfile)

    for linha in reader:
        print(linha)

    csvfile.close()
