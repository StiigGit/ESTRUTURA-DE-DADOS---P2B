# 8. Faça um programa que determine se um número é primo ou não.

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print("O número não é primo.")
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("O número é primo.")
    else:
        print("O número não é primo.")
