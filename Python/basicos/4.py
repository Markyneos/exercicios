def verificarPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = int(input("Digite um número inteiro: "))
if verificarPar(numero):
    print("É par")
else:
    print("Não é par")