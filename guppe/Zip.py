"""
Zip

zip() -> Cria um iterável (Zip object) que agraga elemento de cada um dos iteráveis passados como entrada em pares.
"""
# Exemplos (Ele pega 1° elemento da lista 1, e o 1° da outra, e a string e uni em uma tupla)
# Utilizações como por exemplo pegando as mais tocadas de cada album no spotify e unindo em uma playlist das mais
# tocadas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, "abs")
print(zip1)  # Retorna um zip object at 0x01BEDCC8
print(type(zip1))

# Podemos converter para Listas, tuplas, Sets e dicionários
# OBS: Acontece o mesmo que o map, filter e generator, assim que é convertido ele some da memória, por isso depois
# de converter para lista as demais conversões vieram vazias.
print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))
print("----------------------------------------------------------------------------------------------------------")

# OBS: o zip() utiliza como parâmetro os iteráveis menores, ou seja, quando acabar o iterável menor, ele acaba, exemplo
# Essa última lista não irá contar os ultimos dois valores(10, 11), pois as listas de cimas só tem 3 valores cada.
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
print("---------------------------------------------------------------------------------------------------------")

# Podemos utilizar diferentes tipos de iteráveis
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {"a": 11, "b": 12, "c": 13, "d": 14, "e": 15}
zip1 = zip(tupla, lista, dicionario.values())
print(list(zip1))
print("----------------------------------------------------------------------------------------------------------")

# Exemplo mais complexo
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Alefe', 'Thaylane', 'Ayron']

# DICTIONARY COMPREHESION
# Pega a maior nota de cada aluno(dado[0] -> Pega os alunos, dados[1] -> prova1 e dados[2] -> prova2)
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Utilizando o map para realizar a mesma funçao
finalMap = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(finalMap))








