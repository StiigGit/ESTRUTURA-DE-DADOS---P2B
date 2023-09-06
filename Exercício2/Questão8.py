# 8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado “calcular_media” que retorna a média das notas do aluno.


class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0  # Retorna 0 se não houver notas
        total = sum(self.notas)
        media = total / len(self.notas)
        return media

# Exemplo de uso da classe Aluno
nome_aluno = input("Digite o nome do aluno: ")
notas_aluno = []

quantidade_notas = int(input("Quantas notas você deseja inserir? "))
for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas_aluno.append(nota)

aluno = Aluno(nome_aluno, notas_aluno)
media = aluno.calcular_media()

print(f"A média do aluno {aluno.nome} é: {media:.2f}")