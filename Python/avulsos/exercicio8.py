sal_hora = float(input("Digite quanto você ganha por hora: "))
horas = int(input("Quantas horas você trabalha no mês?: "))
while sal_hora < 1 or horas < 1:
  print("Digite valores válidos!")
  sal_hora = float(input("Digite quanto você ganha por hora: "))
  horas = int(input("Quantas horas você trabalha no mês?: "))

salario = sal_hora * horas
print(f"Seu salário é de R${salario:.2f}")
