# 6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

# Exemplo de uso da classe Produto
nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade_produto = int(input("Digite a quantidade do produto: "))

produto = Produto(nome_produto, preco_produto, quantidade_produto)
total = produto.calcular_total()

print(f"O total a pagar pelo {produto.nome} é: R$ {total:.2f}")