class Carro:
  def __init__(self, modelo: str, cor: str, ano: int):
    self.modelo = modelo
    self.cor = cor
    self.ano = ano
  def __str__(self):
    return f"Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano}"

modelo = input("Digite o modelo de um carro: ")
cor = input("Digite a cor do mesmo carro: ")
ano = int(input("Digite o ano de fabricação desse mesmo carro: "))
carro = Carro(modelo, cor, ano)
print(carro)
