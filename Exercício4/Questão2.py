# 2. Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que
# serve como chave para realizar a ordenação crescente ou decrescente.

def ordenar_vetor(vetor, ordem='crescente'):
    if ordem == 'crescente':
        vetor.sort()
    elif ordem == 'decrescente':
        vetor.sort(reverse=True)
    else:
        print("Ordem inválida. Use 'crescente' ou 'decrescente'.")

# Exemplo de uso:
vetor = [64, 25, 12, 22, 11]

# Ordenar em ordem crescente
ordenar_vetor(vetor, 'crescente')
print("Vetor ordenado em ordem crescente:", vetor)

# Ordenar em ordem decrescente
ordenar_vetor(vetor, 'decrescente')
print("Vetor ordenado em ordem decrescente:", vetor)