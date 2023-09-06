# import numpy as np


# class Listasequencial:
#     def __init__(self, capacidade):
#         self.capacidade = capacidade
#         self.ultima_posicao = -1
#         self.valores = np.empty(self.capacidade, dtype=int)

#     def imprime(self):
#         if self.ultima_posicao == -1:
#             print('o vetor está vazio')
#         else:
#             for i in range(self.ultima_posicao + 1):
#                 print(i, '-', self.valores[i])

#     def insere(self, valor):
#         if self.ultima_posicao == self.capacidade - 1:
#             print('capacidade máxima atingida')
#         else:
#             self.ultima_posicao += 1
#             self.valores[self.ultima_posicao] = valor

#     def pesquisar(self, valor):
#         for i in range(self.ultima_posicao + 1):
#             if (valor == self.valores[i]):
#                 return i
#             return -1

#     def excluir(self, valor):
#         posicao = self.pesquisar(valor)
#         if posicao == -1:
#             return -1
#         else:
#             for i in range(posicao, self.ultima_posicao):
#                 self.valor[i] = self.valores[i + 1]
#         self.ultima_posicao -= 1


# p1 = Listasequencial(5)
# p1.insere(4)
# p1.insere(5)
# p1.insere(6)
# print('==========')
# p1.imprime()








# Crie uma funão que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura e peso


# class CalculaIMC:
#     def __init__(self, peso, altura):
#         self.peso = peso
#         self.altura = altura
#         self.imc = (self.peso/self.altura**2)

#     def imprime(self):
#         print(self.imc)
        




# Escreva um programa que converte uma temperatura de Celsius para Fahrenheit ou vice e versa, dependendo da escolha do usuário.


class ConverteCparaF:
    def __init__ (self, tempc):
        self.tempc = tempc
        self.tempf = 1.8*self.tempc+32

    def imprime(self):
        print(self.tempf)
    
p1=ConverteCparaF (1)
p1.imprime()




class ConverteFparaC:
    def __init__(self, tempf):
        self.tempf = tempf
        self.tempc = 1.8 * self.tempc + 32

    def imprime(self):
        print(self.tempc)


p1 = ConverteFparaC(1)
p1.imprime()

opcao = input("Você quer converter de C para F, ou de F para C? ")
if opcao == 'C para F':
    ConverteCparaF(opcao)
    ConverteCparaF.imprime()
