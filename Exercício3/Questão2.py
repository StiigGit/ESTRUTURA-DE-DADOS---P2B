# 2. Escreva uma função que calcula o fatorial de um número inteiro positivo fornecido pelo usuário.

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero = int(input("Digite um número inteiro positivo: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")