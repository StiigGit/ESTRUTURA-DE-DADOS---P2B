# 4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente métodos “depositar” e “sacar” para manipular o saldo.


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado com sucesso."
        else:
            return "O valor do depósito deve ser maior que zero."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso."
        else:
            return "Saldo insuficiente ou valor de saque inválido."

    def consultar_saldo(self):
        return f"Saldo atual da conta de {self.titular}: R$ {self.saldo:.2f}"

# Exemplo de uso da classe ContaBancaria
conta = ContaBancaria("João")

print(conta.consultar_saldo())
print(conta.depositar(1000))
print(conta.sacar(500))
print(conta.consultar_saldo())