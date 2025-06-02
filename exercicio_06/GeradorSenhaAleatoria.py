import random
import string

def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    try:
        tamanho = int(input("Informe o número de caracteres para a senha: "))
        if tamanho <= 0:
            print("Por favor, informe um número positivo.")
            return
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        print(f"Senha gerada: {senha}")
    except ValueError:
        print("Por favor, insira um número válido.")

gerar_senha()
