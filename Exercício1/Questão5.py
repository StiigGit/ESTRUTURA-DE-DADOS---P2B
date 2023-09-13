# 5. Faça um programa que leia uma lista de números e retorne a média dos números pares.

quantidade = int(input("Quantos números você deseja inserir na lista? "))

for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numeros_pares = [num for num in numeros if num % 2 == 0]

if len(numeros_pares) > 0:
    media_pares = sum(numeros_pares) / len(numeros_pares)
    print(f"A média dos números pares é: {media_pares:.2f}") 
else:
    print("Não há números pares na lista.")