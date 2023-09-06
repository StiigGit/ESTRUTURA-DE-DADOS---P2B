# 2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método chamado “detalhes” que retorna uma string com as informações do livro.


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}"

# Exemplo de uso da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")

print("Detalhes do Livro 1:")
print(livro1.detalhes())

print("\nDetalhes do Livro 2:")
print(livro2.detalhes())