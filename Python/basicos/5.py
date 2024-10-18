print("Insira as 4 notas bimestrais do aluno: ")
notas = []
for i in range(4):
    notas.append(int(input(f"{i + 1}º: ")))

media = 0

for i in range(len(notas)):
    media += notas[i]
media /= len(notas)

ordem = sorted(notas)

print(f"Média: {media:.2f}\nMenor nota: {ordem[0]}\nMaior nota: {ordem[-1]}")