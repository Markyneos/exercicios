def valor(numero):
  if numero >= 1:
    return "P"
  else:
    return "N"

numero = int(input("Digite um número: "))
print(valor(numero))