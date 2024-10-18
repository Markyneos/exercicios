class Bola:
  def __init__(self, cor, circunferencia, material):
    self.cor = cor
    self.circunferencia = circunferencia
    self.material = material
  def trocaCor(self, novaCor):
    self.cor = novaCor
  def mostraCor(self):
    print(self.cor)

bola = Bola("Amarela", 10, "Borracha")
bola.mostraCor()

bola.trocaCor("Vermelha")
bola.mostraCor()
