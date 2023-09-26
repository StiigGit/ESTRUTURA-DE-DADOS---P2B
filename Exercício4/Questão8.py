# 8. Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor do
# meio quando o vetor é ordenado. Certifique-se de que sua função funcione para vetores com um
# número ímpar de elementos.

def calcular_mediana(vetor):
    vetor_ordenado = sorted(vetor)
    tamanho = len(vetor_ordenado)

    if tamanho % 2 == 1:  # Se for ímpar
        mediana = vetor_ordenado[tamanho // 2]
    else:  # Se for par
        meio1 = vetor_ordenado[(tamanho // 2) - 1]
        meio2 = vetor_ordenado[tamanho // 2]
        mediana = (meio1 + meio2) / 2

    return mediana


# Exemplo de uso:
vetor = [64, 25, 12, 22, 11, 8, 7]

mediana = calcular_mediana(vetor)
print("Mediana:", mediana)
