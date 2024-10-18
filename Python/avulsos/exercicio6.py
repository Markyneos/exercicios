import math

print("Digite o valor do raio de um círculo: ")
raio = float(input())
if raio > 0:
  area = math.pi * math.pow(raio, 2)
  print(f"A área do círculo de raio {raio} é aproximadamente: {area:.2f}")
else:
  print("Digite um valor válido!")
  