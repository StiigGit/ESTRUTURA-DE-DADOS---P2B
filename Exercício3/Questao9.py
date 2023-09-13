# 9. Crie uma calculadora que realiza operações de adição, subtração, multiplicação e divisão, com base na escolha do usuário.

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Divisão por zero não é permitida."
    return x / y

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = int(input("Digite o número da operação: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    print(f"Resultado: {soma(num1, num2)}")
elif opcao == 2:
    print(f"Resultado: {subtracao(num1, num2)}")
elif opcao == 3:
    print(f"Resultado: {multiplicacao(num1, num2)}")
elif opcao == 4:
    print(f"Resultado: {divisao(num1, num2)}")
else:
    print("Opção inválida")