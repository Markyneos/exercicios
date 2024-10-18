class Estudante:
  def __init__(self, nome: str, idade: int, matricula: int):
    self.nome = nome
    self.idade = idade
    self.matricula = matricula
  def __str__(self) -> str:
    return f"Nome: {self.nome} | Idade: {self.idade} | Matrícula: {self.matricula}"
  def adicionarNota(self, novaNota: float) -> None:
    self.nota = novaNota
  def mostrarNota(self) -> None:
    print(self.nota)


pessoa = Estudante("Marco", 19, 2024242942)
print(pessoa)
pessoa.adicionarNota(5)
pessoa.mostrarNota()
