import math

lado = float(input("Digite o valor do lado de um quadrado: "))
while lado < 1:
  print("Digite um valor válido!")
  lado = float(input("Digite o valor do lado de um quadrado: "))
area = math.pow(lado, 2)
dobro = area * 2
print(f"A área do quadrado de lado {lado} e seu dobro, respectivamente: {area:.2f}, {dobro:.2f}")