#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

#BUG:
nome = ''
senha = ''
#TODO:
while nome == senha:
  nome = input("Digite seu nome de usuário: ")
  senha = input("Digite sua senha: ")
  if nome == senha:
    print("Erro: Sua senha não pode ser igual ao nome de usuário!")
  else:
    print("Cadastro concluído!")
