# 3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método chamado “calcular_area” que retorna a área do retângulo.


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Exemplo de uso da classe Retangulo
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

retangulo = Retangulo(base, altura)
area = retangulo.calcular_area()

print(f"A área do retângulo é: {area:.2f}")