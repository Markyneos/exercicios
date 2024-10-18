def listar(n):
  valores = list(range(1, n + 1))
  valores2 = []
  for i in range(len(valores)):
    valores2.append(str(valores[i]) + " ")
    valores2[i] = valores2[i] * valores[i]
  return valores2


n = int(input("Digite um valor inteiro: "))
lista = listar(n)
for i in lista:
  print(i)

