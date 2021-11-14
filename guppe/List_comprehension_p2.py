"""
List comprehension pt2

Nós podems adicionar estruturas condicionais lógicas
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refatorando(0 é false, e not false é igual a True)
paresRef = [numero for numero in numeros if not numero % 2]
# 
imparesRef = [numero for numero in numeros if numero % 2]
print(paresRef)
print(imparesRef)
