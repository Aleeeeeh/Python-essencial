"""
List comprehension

- Utilizando list comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe
[dado for dado in iterável]

"""
# Exemplos
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

"""
# Para entender melhor, vamos dividir em duas partes
 - Primeira parte: numero * 10
 - Segunda parte: for numero in numeros
 
"""


def funcao(valor):
    return valor * valor


res2 = [funcao(numero) for numero in numeros]
print(res2)

# List comprehension vs loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List comprehension (Em uma linha foi feito o mesmo que o laço for acima)
print([numero * 2 for numero in numeros])

# Mais exemplos
nome = "Geek University"
print([letra.upper() for letra in nome])

# Primeira letra de cada nome deixa maiusculo


def caixa_alta(nome):
    letramaior = nome.replace(nome[0], nome[0].upper())
    return letramaior


familia = ['alefe', 'Thaylane', 'Ayron']
print([caixa_alta(membro) for membro in familia])

# Percorrendo a lista e verificando se é verdadeiro ou falso com bool
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Pega uma lista de inteiros e converte para uma lista de strings
print([str(valor) for valor in [1, 2, 3, 4, 5]])








