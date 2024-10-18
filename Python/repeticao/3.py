#Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

def validar(nome: str, idade: int, salario: float, sexo: str, ec: str) -> bool:
  if len(nome) <= 3:
    print("O nome deve ter mais de 3 caracteres!")
    return True
  if idade <= 0 or idade >= 150:
    print("Sua idade não deve ser menor que 1 ou maior que 150!")
    return True
  if salario <= 0.0:
    print("Seu salário deve ser maior que 0!")
    return True
  if sexo != 'f' and sexo != 'm':
    print("Sexo inválido!")
    return True
  if ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
    print("Digite um estado civíl válido!")
    return True
  return False
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo(m/f): ")
ec = input("Digite seu estado civíl(s/c/v/d): ")

while validar(nome, idade, salario, sexo, ec):
  nome = input("Digite seu nome: ")
  idade = int(input("Digite sua idade: "))
  salario = float(input("Digite seu salário: "))
  sexo = input("Digite seu sexo(m/f): ")
  ec = input("Digite seu estado civíl(s/c/v/d): ")
print("Dados validados com sucesso")
