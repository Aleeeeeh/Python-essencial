"""
Dictionary comprehension
-- Sintaxe
{chave: valor for in i iterável}

"""
# Exemplos
numeros = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)  # {'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}

# Iterando sobre listas
lista = [1, 2, 3, 4, 5, 6]
quadLista = {valor: valor ** 2 for valor in lista}
print(quadLista)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# Obs: Se colocassemos chaves iguais na lista, o dicionário não iria contar

# Mais exemplos
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Exemplos com lógica condicional
numeros = [1, 2, 3, 4, 5]
verificaNumero = {num: ("Par" if num % 2 == 0 else "Impar") for num in numeros}
print(verificaNumero)








