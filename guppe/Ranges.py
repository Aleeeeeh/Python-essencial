"""
Ranges são usadas para gerar sequências numéricas,não de forma aleatória, mas sim de maneira especificada

Formas gerais:
range(inicio padrao 0, limitador, passo)

Convertendo range em lista para exibir no console
lista = list(range(10))
print(lista)
"""

# Quando queremos escolher o valor inicial colocamos os dois valores
for num in range(1, 11):
    print(num)

# Especificando o passo
for num in range(1, 10, 2):
    print(num)

# Decrementando
for num in range(10, 0, -1):
    print(num)

