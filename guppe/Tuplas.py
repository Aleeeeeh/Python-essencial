"""
Tuplas(tuple)

Tuplas são bastante parecidas com listas.Por quê utilizar tuplas?
1 - Tuplas são mais rápidas do que listas.
2 - Deixa o código mais seguro, pois trabalhar com elementos imutáveis traz segurança para o código

Existem basicamente duas diferenças:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis, ou seja se criar um tupla ela não muda, Toda operação em uma tupla gera uma
nova tupla.

3 - Slicing e a forma de acessar um elemento da lista através do indice como print(exemplo[3]) é exatamente
igual as listas entre outras coisas consultar no arquivo de listas

Exemplos:
tupla = (1, 2, 3)
print(type(tupla))

Sem parênteses também é considerado uma tupla
tupla1 = 1, 2, 3
print(type(tupla1))

Para ser considerado uma tupla deve ter número e virgula, ou seja com 1 valor deve ficar assim:
(4,) -> Tuple
Caso contrário
tupla2 = (4)
print(type(tupla2)) -> int

Não conseguimos adicionar ou remover elementos nas tuplas justamente por serem imutáveis.
 - SOMA, MAXIMO, MINIMO, LEN (Feito da mesmo forma que é feita em listas)

 Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados em uma coleção, exemplo uma tupla
 de meses, não iriamos que nem nós nem ninguém adicionasse mês, pois ja são padrão de 12 meses
"""
# Podemos gerar uma tupla dinamicamente usando range, e também a função 'tuple'
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacontamento de tupla
tupla = ('Python', 'Geek university')
curso, escola = tupla
print(escola)
print(curso)

# Concatenando tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(tupla1 + tupla2)

# Tuplas são imutáveis mas podemos sobrescrever seus valores
tupla1 = (21, 23, 1)
print(tupla1)

# Contagem de elementos dentro da tupla
tupla4 = (1, 2, 5, 6, 2, 7, 5, 10, 10)
print(tupla4.count(10))

# Tranformando string em tupla, semelhante as listas
tupla5 = tuple('Alefe')
print(tupla5)



