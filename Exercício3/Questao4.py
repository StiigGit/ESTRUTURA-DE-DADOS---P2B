# 4. Escreva um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.

def soma_digitos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10
    return soma

numero = int(input("Digite um número inteiro positivo: "))
resultado = soma_digitos(numero)
print(f"A soma dos dígitos de {numero} é {resultado}")