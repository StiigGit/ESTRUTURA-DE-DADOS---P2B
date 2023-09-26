# 4. Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.

def segundo_menor(vetor):
    if len(vetor) < 2:
        return None  # Retorna None se houver menos de dois elementos

    menor = float('inf')  # Inicializa com infinito positivo
    segundo_menor = float('inf')  # Inicializa com infinito positivo

    for numero in vetor:
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif numero < segundo_menor and numero != menor:
            segundo_menor = numero

    return segundo_menor


# Exemplo de uso:
vetor = [64, 25, 12, 22, 11, 12, 22]

segundo_menor_numero = segundo_menor(vetor)
if segundo_menor_numero is not None:
    print("Segundo menor número:", segundo_menor_numero)
else:
    print("Não há segundo menor número.")
