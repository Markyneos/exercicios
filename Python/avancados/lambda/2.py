numero = int(input("Digite um número qualquer: "))

parImpar = lambda numero: True if numero % 2 == 0 else False

if parImpar(numero):
    print("O número é par")
else:
    print("O número é impar")