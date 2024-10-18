class Quadrado:
  def __init__(self, tamanho):
    self.lado = tamanho
  def mudarLado(self, novo_tamanho):
    self.lado = novo_tamanho
  def retornarLado(self) -> float | int:
    return self.lado
  def calcularArea(self):
    return self.lado * self.lado

quadradin = Quadrado(5)

print(quadradin.retornarLado())
quadradin.mudarLado(10)
print(quadradin.retornarLado())
area = quadradin.calcularArea()
print(area)
