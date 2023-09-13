# 10. Escreva uma função que gera a sequência de Fibonacci até um determinado número de termos especificado pelo usuário.

def gerar_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)
    return fibonacci

termos = int(input("Digite o número de termos da sequência de Fibonacci: "))
sequencia = gerar_fibonacci(termos)
print(f"Sequência de Fibonacci com {termos} termos: {sequencia}")