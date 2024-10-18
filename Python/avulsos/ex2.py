#Você fez uma pequena pesquisa de preferência entre três produtos A, B e C. Na entrevista, cada entrevistado precisava escolher seu produto preferido. Agora, seu objetivo é calcular qual produto foi o mais votado. A partir da lista de votos, crie um dicionário onde a chave é cada produto, e o valor é o número de votos que o produto recebeu.

votos = {
  'A': 0,
  'B': 0,
  'C': 0
}

pesquisa = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

for i in pesquisa:
  votos[i] += 1

print(f"Votos em A: {votos['A']} | Votos em B: {votos['B']} | Votos em C: {votos['C']}")
