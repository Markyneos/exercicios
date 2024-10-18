'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros 
formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e 
custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para
incluir o imposto sobre vendas.
'''
def somaImposto(taxa, custo):
  novo_valor = ((taxa / 100) * custo) + custo
  return novo_valor

taxa = int(input("Digite a taxa de imposto sobre o produto(%): "))
custo = float(input("Digite o valor do produto: "))
print(f"O novo valor do produto é R${somaImposto(taxa, custo):.2f}")