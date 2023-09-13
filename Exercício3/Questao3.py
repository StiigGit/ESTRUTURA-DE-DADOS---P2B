# 3. Crie uma função que verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, desconsiderando espaços e pontuação).

def eh_palindromo(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]

frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")


