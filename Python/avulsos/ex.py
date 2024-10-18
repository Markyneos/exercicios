#Nesta atividade, você possui uma lista de números qualquer. Seu objetivo é encontrar o segundo maior valor da lista (supondo que ela possua pelo menos dois elementos).


def segundoMaior(lista: list) -> int:
  return sorted(lista)[-2]


if __name__ == '__main__':
  resultado = ''
  numeros = [32, 10, 58, 30, 55, 12, 28, 51]
  for i in range(len(numeros)):
    resultado = resultado + str(numeros[i]) + ' '
  print(f"Lista: {resultado}")
  print(f"O segundo maior número da lista é: {segundoMaior(numeros)}")
