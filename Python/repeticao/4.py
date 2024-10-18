# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# a = 80000.0
# b = 200000.0
# contador = 0

def crescimento(a: float, taxa: float) -> float:
  a = a + (a * taxa)
  return a

# while a < b:
#   a = crescimento(a, 0.03)
#   b = crescimento(b, 0.015)
#   contador += 1
#   if a > b:
#     print(f"População da cidade A: {a:.2f} | População da cidade B: {b:.2f}\nAnos que se passaram: {contador} anos")


#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

cidade1 = int(input("Digite o número de habitantes da cidade 1: "))
cidade2 = int(input("Digite o núemero de habitantes da cidade 2: "))
taxa1 = float(input("Digite a taxa de crescimento da cidade 1: ")) / 100
taxa2 = float(input("Digite a taxa de crescimento da cidade 2: ")) / 100
contador = 0

if cidade1 < cidade2 and taxa1 > taxa2:

  while cidade1 < cidade2:
    cidade1 = crescimento(cidade1, taxa1)
    cidade2 = crescimento(cidade2, taxa2)
    contador += 1
    if cidade1 > cidade2:
      print(f"População da cidade 1: {cidade1:.0f} | População da cidade 2: {cidade2:.0f}\nAnos que se passaram para a cidade 1 chegar à cidade2: {contador} anos")
      break
elif cidade1 < cidade2 and taxa1 < taxa2:
    print("Erro! Caso a cidade 2 tenha mais habitantes que a cidade 1 a taxa de crescimento da cidade 1 deve ser maior que a da cidade 2!")
elif cidade1 > cidade2 and taxa1 < taxa2:

  while cidade1 > cidade2:
    cidade1 = crescimento(cidade1, taxa1)
    cidade2 = crescimento(cidade2, taxa2)
    contador += 1
    if cidade1 < cidade2:
      print(f"População da cidade 1: {cidade1:.0f} | População da cidade 2: {cidade2:.0f}\nAnos que se passaram para que a cidade 2 chegasse à cidade 1: {contador} anos")
      break
elif cidade1 > cidade2 and taxa1 > taxa2:
    print("Erro! Caso a cidade 1 tenha mais habitantes que a cidade 2 a taxa de crescimento da cidade 2 deve ser maior que a da cidade 1!")
