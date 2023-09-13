# 7. Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura e peso.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

imc = calcular_imc(peso, altura)
print(f"Seu IMC é {imc:.2f}")