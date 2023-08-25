# 9. Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.

nomes = []

quantidade = int(input("Quantos nomes você deseja inserir na lista? "))

for i in range(quantidade):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

nomes_com_a = [nome for nome in nomes if nome.startswith('A') or nome.startswith('a')]

print("Nomes que começam com 'A':")
for nome in nomes_com_a:
    print(nome)
