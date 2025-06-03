#Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.​

import csv 

with open("atividade-02.csv", "w", newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['Nome', 'Idade', 'Cidade'])  # Cabeçalho
    writer.writerow(['Maria', 40, 'Rio de Janeiro'])
    writer.writerow(['João', 25, 'São Paulo'])
    writer.writerow(['Fernanda', 23, 'Rio Grande do Sul'])
    writer.writerow(['Marcos', 30, 'Pernambuco'])

    csvfile.close()