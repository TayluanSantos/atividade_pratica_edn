# Crie um programa para o professor registrar as notas da turma.
# Regras:
# Continuar solicitando notas até que o professor digite 'fim'.
# Aceitar apenas notas entre 0 e 10.
# Ignorar notas inválidas e continuar solicitando.
# Ao final, mostrar a média da turma.

qtd_notas = []
soma_notas = 0

while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ").strip().lower()
    
    if entrada == "fim":
        break

    try:
        nota = float(entrada)
        if (0 <= nota <= 10):
            qtd_notas.append(nota)
            soma_notas += nota
        else:
            print("Nota inválida. Por favor, insira uma nota de 0 a 10.")
    except ValueError:
        print("Entrada inválida. Por favor, insira uma nota numérica ou 'fim' para sair.")

if (len(qtd_notas) > 0 ):
    media = soma_notas / len(qtd_notas)
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")
