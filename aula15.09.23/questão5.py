# 5. Implemente uma função que aceite um vetor de números inteiros e remova todos os elementos
# duplicados, retornando o vetor resultante sem duplicatas.

def remove_duplicatas(vetor):
    vetor_sd = []
    for elemento in vetor:
        if elemento not in vetor_sd:
            vetor_sd.append(elemento)
    return vetor_sd

vetor=[5,7,4,4,7,3]
print(vetor)
print(remove_duplicatas(vetor))
