# 6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

número.
numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é: {fatorial}")
