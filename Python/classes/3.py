class Retangulo:
  def __init__(self, base: int | float, altura: int | float):
    self.base = base
    self.altura = altura
  def mudarValores(self, novaBase: int | float, novaAltura: int | float) -> None:
    self.base = novaBase
    self.altura = novaAltura
  def retornarLados(self) -> tuple:
    return self.base, self.altura
  def calcularArea(self) -> int | float:
    return self.base * self.altura
  def calcularPerimetro(self) -> int | float:
    return (2 * self.base) + (2 * self.altura)



if __name__ == '__main__':
  print("Informe as medidas de um terreno")
  base = float(input("Digite o valor da base: "))
  altura = float(input("Digite o valor da altura: "))
  terreno = Retangulo(base, altura)
  print(f"Quantidade de pisos necessários: {terreno.calcularArea()} (m²)\nQuantidade de rodapés necessários: {terreno.calcularPerimetro()} (m)")

