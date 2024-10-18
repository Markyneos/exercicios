class Carro:
  def __init__(self, consumoKmL: float, combustivel=0.0):
    self.consumoKmL = consumoKmL
    self.combustivel = combustivel
  def andar(self, distancia: float) -> None:
    if self.combustivel - (distancia / self.consumoKmL) >= 0:
      self.combustivel -= (distancia / self.consumoKmL)
      print(f"O carro andou {distancia}km!")
    elif self.combustivel - (distancia / self.consumoKmL) < 0 and self.combustivel > 0:
      self.combustivel = 0
      print("O combustível acabou!")
      print("A trajetória não pode ser completada.")
  def obterGasolina(self) -> float:
    return self.combustivel
  def adicionarGasolina(self, quantidadeAdicionada: float) -> None:
    self.combustivel += quantidadeAdicionada


meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
print(f"{meuFusca.obterGasolina()}L")
