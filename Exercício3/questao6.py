# 6. Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes nela.

def contar_vogais(string):
    vogais = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vogais:
            count += 1
    return count

string = input("Digite uma string: ")
vogais = contar_vogais(string)
print(f"A string contém {vogais} vogais.")