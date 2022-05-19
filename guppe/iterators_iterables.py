"""
Entendendo como funciona a iteração por debaixo dos panos

Iterator ->
    - Um objeto que pode ser iterado.
    - No laço for quando percorremos um elemento, estamos dando vários next()

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada, ou seja, no momento que pegamos
    o elemento a ser iterado.
"""
nome = "Geek"
numeros = [1, 2, 3, 4, 5]

# Iterable -> retornando um iterator
it1 = iter(nome)
it2 = iter(numeros)

# Iterator -> Percorrendo o elemento, depois de transformado pelo iterable
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it1)) -> Ultrapassando o limite emite o erro StopIteration, no laço for padrão ele para sozinho
print("-----------------------")

for letra in nome:
    print(letra)



