"""
Map

Com map, fazemos mapeamento de valores para função.
"""
import math


def area(r):
    """Cálcula a área de um raio 'r'"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

# Forma comum
raios = [2, 5, 7.1, 0.3, 10, 44]
areas = []

for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 com Map

# Map é uma função que recebe dois parâmetros: o primeiro a função, o segundo um iterável. retorna um map object
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 com lambdas
print(list(map(lambda x: math.pi * (x ** 2), raios)))
# OBS: No map Convertemos para lista apenas na primeira vez, quando executar novamente, a lista zera.

# Mais um exemplo, partindo de uma lista de tuplas
cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19)]

print(cidades)
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))





