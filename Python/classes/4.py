#Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
  def __init__(self, nome: str, idade: int, peso: float, altura: float):
      self.nome = nome
      self.idade = idade
      self.peso = peso
      self.altura = altura
  def __str__(self):
    return f"Nome: {self.nome} | Idade: {self.idade} | Peso: {self.peso:.2f}kg | Altura: {self.altura:.2f}m"
  def envelhecer(self, anosEnvelhecidos: int) -> None:
    if anosEnvelhecidos < 0:
      print("Uma pessoa não consegue rejuvenescer!")
    else:
      self.idade += anosEnvelhecidos
      self.altura += (anosEnvelhecidos * 0.05) if self.idade < 21 else 0
  def engordar(self, pesoGanho: float) -> None:
    self.peso += pesoGanho
  def emagrecer(self, pesoPerdido: float) -> None:
    self.peso -= pesoPerdido
  def crescer(self, alturaGanha: float) -> None:
    self.altura += alturaGanha


if __name__ == '__main__':
  nome = input("Digite seu nome (ou de uma pessoa qualquer): ")
  idade = int(input("Digite a idade da pessoa em questão: "))
  peso = float(input("Digite o peso dessa mesma pessoa (em quilos): "))
  altura = float(input("Digite a altura dessa pessoa (em metros): "))
  pessoa1 = Pessoa(nome, idade, peso, altura)
  while True:
    print("Você deseja...?:")
    print("1. Envelhecer a pessoa\n2. Engordar a pessoa\n3. Emagrecer a pessoa\n4. Fazê-la crescer\n5. Exibir os dados da pessoa\n0. Sair")
    escolha = input("Escolha: ")
    match escolha:
      case '1':
        anos = int(input("Quantos anos você deseja fazer com que ela envelheça: "))
        pessoa1.envelhecer(anos)
      case '2':
        kilos = float(input("Quantos quilos você deseja fazê-la(o) engordar: "))
        pessoa1.engordar(kilos)
      case '3':
        kilos = float(input("Quantos quilos você deseja fazê-la(o) emagrecer: "))
        pessoa1.emagrecer(kilos)
      case '4':
        metros = float(input("Quantos metros você deseja fazer com que ele/ela cresça: "))
        if pessoa1.altura + metros >= 3:
          print("Essa altura ainda não foi alcançada por nenhum humano, por favor digite uma altura mais comum")
        else:
          pessoa1.crescer(metros)
      case '5':
        print(pessoa1)
      case '0':
        print("AVISO: TODOS OS DADOS SERÃO PERDIDOS")
        escolha2 = input("Deseja continuar? (y/n): ")
        if escolha2 == 'y':
          break
        elif escolha2 == 'n':
          pass
        else:
          print("Resposta não identificada")
      case _:
        print("Resposta não identificada")
