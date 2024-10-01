numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print(quadrados)

#Aninhando Loops
#Você também pode aninhar for dentro de compreensões de lista.
#Por exemplo, para criar uma lista de combinações de duas listas:
lista1 = [1, 2]
lista2 = ['a', 'b']
combinacoes = [(x, y) for x in lista1 for y in lista2]
print(combinacoes)