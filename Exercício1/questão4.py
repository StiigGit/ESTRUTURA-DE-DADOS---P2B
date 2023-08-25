# 4. Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

numeros = []

quantidade = int(input("Quantos números você deseja inserir na lista? "))

for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f"O maior valor da lista é: {maior}")
print(f"O menor valor da lista é: {menor}")
