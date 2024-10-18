class BombaCombustivel:
  def __init__(self, tipoCombustivel: str, valorLitro: float, quantidadeCombustivel:float):
    self.tipoCombustivel = tipoCombustivel
    self.valorLitro = valorLitro
    self.quantidadeCombustivel = quantidadeCombustivel
  def __str__(self) -> str:
    return f"{self.tipoCombustivel}, {self.valorLitro}, {self.quantidadeCombustivel}"
  def abastecerPorValor(self, valor: float) -> float:
    self.quantidadeCombustivel -= valor / self.valorLitro
    return valor / self.valorLitro
  def abastecerPorLitro(self, litragem: float) -> float:
    self.quantidadeCombustivel -= litragem
    return litragem * self.valorLitro
  def alterarValor(self, novoValor: float) -> None:
    self.valorLitro = novoValor
  def alterarCombustivel(self, novoTipo: str) -> None:
    self.tipoCombustivel = novoTipo
  def alterarQuantidadeCombustivel(self, novaQuantidade: float) -> None:
    self.quantidadeCombustivel = novaQuantidade

objeto = BombaCombustivel("Diesel", 5.50, 50)
print(objeto)
objeto.alterarQuantidadeCombustivel(100)
print(objeto)
