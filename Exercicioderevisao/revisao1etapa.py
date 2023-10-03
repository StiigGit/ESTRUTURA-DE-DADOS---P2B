import numpy as np
import random
import time

# Função para gerar um vetor de tamanho especificado com números aleatórios
def gerar_vetor(tamanho):
    return [random.randint(1, 1000000) for _ in range(tamanho)]

# Função para ordenar um vetor e medir o tempo gasto
def ordenar_vetor(vetor):
    inicio = time.time()  # Marca o tempo inicial
    vetor.sort()          # Ordena o vetor
    fim = time.time()    # Marca o tempo final
    return fim - inicio  # Retorna o tempo gasto em segundos

# Gere um vetor de 10.000 números aleatórios
tamanho_vetor = 10000
vetor_aleatorio = gerar_vetor(tamanho_vetor)

# Ordene o vetor e meça o tempo gasto
tempo_gasto = ordenar_vetor(vetor_aleatorio)

print(f"Tempo gasto para ordenar o vetor de {tamanho_vetor} números: {tempo_gasto:.6f} segundos")

