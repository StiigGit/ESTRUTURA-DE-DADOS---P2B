# 10. Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento > 0:
            aumento = (percentual_aumento / 100) * self.salario
            self.salario += aumento
            return f"Salário do {self.nome} atualizado para R$ {self.salario:.2f}"
        else:
            return "O percentual de aumento deve ser maior que zero."

# Exemplo de uso da classe Funcionario
nome_funcionario = input("Digite o nome do funcionário: ")
salario_funcionario = float(input("Digite o salário do funcionário: "))
cargo_funcionario = input("Digite o cargo do funcionário: ")

funcionario = Funcionario(nome_funcionario, salario_funcionario, cargo_funcionario)

percentual_aumento = float(input("Digite o percentual de aumento salarial: "))
mensagem = funcionario.aumentar_salario(percentual_aumento)

print(mensagem)
print(f"Novo salário do {funcionario.nome}: R$ {funcionario.salario:.2f}")