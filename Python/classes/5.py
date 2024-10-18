class ContaCorrente:
  def __init__(self, num_conta: int, nome_correntista: str, saldo=0.0):
    self.num_conta = num_conta
    self.nome = nome_correntista
    self.saldo = saldo
  def __str__(self):
    return f"Número da conta: {self.num_conta} | Nome do Correntista: {self.nome} | Saldo: R${self.saldo:.2f}"
  def alterarNome(self, novoNome: str) -> None:
    self.nome = novoNome
  def deposito(self, adicao:float) -> None:
    self.saldo += adicao
  def saque(self, dinheiro:float) -> None:
    self.saldo -= dinheiro

conta = ContaCorrente(123654, "Roberto Carlos", 5000.0)
print(conta)
conta.deposito(10000)
print(conta)
conta.alterarNome("Tim Maia")
conta.saque(5000)
print(conta)
