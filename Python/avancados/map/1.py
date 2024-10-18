'''Map() é uma função que permite aplicar uma função a todos os itens
 de uma sequência (como uma lista) e retornar uma nova sequência com os resultados'''
 
temperatura_celsius = [22.5, 40, 13, 29, 34]
temperaturas_fahrenheit = list(map(lambda temp: round((9 / 5) * temp + 32, 1), temperatura_celsius))
print(temperaturas_fahrenheit)