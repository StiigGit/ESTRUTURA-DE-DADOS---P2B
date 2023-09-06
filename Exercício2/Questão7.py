# 7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método chamado “detalhes” que retorna uma string com as informações do carro.


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"

# Exemplo de uso da classe Carro
marca_carro = input("Digite a marca do carro: ")
modelo_carro = input("Digite o modelo do carro: ")
ano_carro = input("Digite o ano do carro: ")

carro = Carro(marca_carro, modelo_carro, ano_carro)
informacoes_carro = carro.detalhes()

print("Detalhes do Carro:")
print(informacoes_carro)