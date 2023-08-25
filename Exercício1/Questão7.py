# 7. Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

limite = int(input("Digite o valor limite para a sequência de Fibonacci: "))

a, b = 0, 1
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b
