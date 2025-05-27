import re

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()

    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break

    # Verifica se a senha tem pelo menos 8 caracteres e contém ao menos um número
    if len(senha) >= 8 and re.search(r'\d', senha):
        print("Senha forte! Acesso permitido.")
        break
    else:
        print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter ao menos um número.")
