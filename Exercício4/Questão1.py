# 1. Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o
# algoritmo de seleção.

def ordenar_por_selecao(vetor):
    n = len(vetor)

    for i in range(n - 1):
        indice_minimo = i

        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j

        # Trocar os elementos
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]


# Exemplo de uso
vetor = [64, 25, 12, 22, 11]
ordenar_por_selecao(vetor)
print("Vetor ordenado:", vetor)
