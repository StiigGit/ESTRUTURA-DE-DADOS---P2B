# 5. Implemente uma função que aceite um vetor de números inteiros e remova todos os elementos
# duplicados, retornando o vetor resultante sem duplicatas.

def remover_duplicatas(vetor):
    vetor_sem_duplicatas = list(set(vetor))
    return vetor_sem_duplicatas

# Exemplo de uso:
vetor = [1, 2, 2, 3, 4, 4, 5]

vetor_sem_duplicatas = remover_duplicatas(vetor)
print("Vetor sem duplicatas:", vetor_sem_duplicatas)
