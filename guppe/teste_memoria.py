"""
Teste de Memória com Generators


# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Teste 1 Lista
for n in fib_lista(100000):
    print(n)

# Funções geradoras consomem menos memória, pois funciona sobe demanda, ou seja, cada vez que percorre um dado
de uma coleção ela não sai, e espera da um next() pra voltar pra cima, enquanto que uma função comum percorre
tudo de uma vez, e retorna.
"""

# Função usando listas 449MB


def fib_lista(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


# Função usando geradores

def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 1 function com return 463,6 MB
for x in fib_lista(100000):
    print(x)

# Teste 2 Geradores Máx 3MB de consumo
for n in fib_gen(100000):
    print(n)
