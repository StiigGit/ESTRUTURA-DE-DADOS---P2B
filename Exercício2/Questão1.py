# 1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado “calcular_area” que retorna a área do círculo.


import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        return area

# Exemplo de uso da classe Circulo
raio_circulo = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio_circulo)
area = circulo.calcular_area()
print(f"A área do círculo é: {area:.2f}")