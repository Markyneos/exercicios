if __name__ == '__main__':
  print("Digite um valor em metros para ser convertido em centímetros:")
  valor = float(input())
  if valor > 0:
    valor *= 100
    print(f"O valor digitado em centímetros é {valor}")
  else:
    print("Digite um valor válido!")
    