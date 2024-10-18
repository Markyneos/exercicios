print("Digite as 4 notas bimestrais do aluno: ")
notas = []
for i in range(4):
    notas.append(int(input(f"{i + 1}º: ")))

media = 0

for i in range(len(notas)):
    media += notas[i]
media /= len(notas)

print(f"Média: {media}")
if media >= 7:
    print("APROVADO(A)")
else:
    print("REPROVADO(A)")