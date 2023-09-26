# 7. Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.

def terceiro_maior(vetor):
    if len(vetor) < 3:
        return None  # Retorna None se houver menos de três elementos

    # Remove duplicatas usando um conjunto (set) e converte de volta para uma lista
    vetor_sem_duplicatas = list(set(vetor))

    if len(vetor_sem_duplicatas) < 3:
        return None  # Retorna None se houver menos de três elementos únicos

    # Ordena o vetor em ordem decrescente
    vetor_sem_duplicatas.sort(reverse=True)

    return vetor_sem_duplicatas[2]  # O terceiro maior é o terceiro elemento na lista ordenada


# Exemplo de uso:
vetor = [64, 25, 12, 22, 11, 25, 12, 22]

terceiro_maior_numero = terceiro_maior(vetor)
if terceiro_maior_numero is not None:
    print("Terceiro maior número:", terceiro_maior_numero)
else:
    print("Não há terceiro maior número.")
