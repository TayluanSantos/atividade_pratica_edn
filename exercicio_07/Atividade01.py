
import csv
import math

tempos = []
with open("logs_treinamento.csv", newline='', encoding='utf-8') as csvfile:
    leitor = csv.DictReader(csvfile)
    for linha in leitor:

        tempo = float(linha['tempo_execucao'])
        tempos.append(tempo)


media = sum(tempos) / len(tempos)
desvio_padrao = math.sqrt(sum((x - media) ** 2 for x in tempos) / (len(tempos) - 1))

print(f"Média dos tempos de execução: {media:.2f} segundos")
print(f"Desvio padrão: {desvio_padrao:.2f} segundos")

csvfile.close()







