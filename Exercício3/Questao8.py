# 8. Escreva um programa que converte uma temperatura em Celsius para Fahrenheit ou vice-versa, dependendo da escolha do usuário.
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Escolha a opção de conversão:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

opcao = int(input("Digite o número da opção: "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius são equivalentes a {fahrenheit:.2f} graus Fahrenheit.")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit são equivalentes a {celsius:.2f} graus Celsius.")
else:
    print("Opção inválida")