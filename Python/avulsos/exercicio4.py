notas = []
print("Insira as 4 notas bimestrais:")
for _ in range(4):
  notas.append(int(input()))

media = 0
for i in range(len(notas)):
  media += notas[i]
media /= 4
print(f"A média das notas bimestrais é {media}")