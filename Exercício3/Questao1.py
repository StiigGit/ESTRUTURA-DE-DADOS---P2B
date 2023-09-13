# 1. Escreva um programa que recebe cinco notas de um aluno e calcula a média. Em seguida, exiba se o aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).

def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = calcular_media(notas)

if media >= 7:
    print(f"Média: {media:.2f} - Aprovado")
else:
    print(f"Média: {media:.2f} - Reprovado")