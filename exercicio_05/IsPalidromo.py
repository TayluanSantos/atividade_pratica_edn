#Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação)

def is_palindromo(palavra):

    palavra = palavra.lower()

    palavra_reversa = palavra[::-1]

    if palavra == palavra_reversa:
        print("Sim")
    else:
        print("Nao")

is_palindromo("casaco")
