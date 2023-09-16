def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def encontrar_max_min(vetor):
    minimo = vetor[0]
    maximo = vetor[0]
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento
        if elemento > maximo:
            maximo = elemento
    return maximo, minimo
