numeros = ([21, 5, 34, 8, 16, 7, 3])

pares = [i for i in numeros if i % 2 == 0]
impares = [i for i in numeros if i % 2 != 0]
somap = 0
somai = 0

for i in pares:
    somap += i
for i in impares:
    somai += i
    
print(somap, somai)