class Tamagushi:
  def __init__(self, nome: str, idade: int, fome=0, saude=100):
    self.nome = nome
    self.idade = idade
    self.fome = fome
    self.saude = saude
  def alterarNome(self, novoNome: str) -> None:
    self.nome = novoNome
  def alterarFome(self, novoValor=0) -> None:
    if novoValor == 0:
      self.fome += 5
    else:
      self.fome = novoValor
  def alterarSaude(self, novoValor:int) -> None:
    self.saude = novoValor
  def alterarIdade(self, novoValor: int) -> None:
    self.idade = novoValor


  def retornarNome(self) -> str:
    return self.nome
  def retornarFome(self) -> int:
    return self.fome
  def retornarSaude(self) -> int:
    return self.saude
  def retornarIdade(self) -> int:
    return self.idade


