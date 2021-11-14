"""
Filter

Filter() -> Serve para filtrar dados de uma determinada coleção.
"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados por algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)  # Mesma coisa de media = (sum(dados) / len(dados))
print(media)

# Obs: Assim com a função map(), o filter() também recebe dois parãmetros uma função e um iterável
res = filter(lambda x: x > media, dados)
print(res)
print(list(res))

# Obs: Assim como na função map, após ser chamado pela primeira vez já convertida em lista,
# na segunda já vem uma lista vazia, como se fosse uma mensagem secreta que se auto destrói

# Ter dados vazios pode atrapalhar e trazer resultados destorcidos na análise de dados
# com filter podemos tirar facilmente esses espaços vazios
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

res = filter(None, paises)
print(list(res))

# A diferença entre map e filter
# O map recebe dois parâmetros e retorna os valores da função passada
# O Filter também recebe dois parâmetros, porém retorna os valores que resultarem em True
# pois o filter ele valida se a informação é True ou False e retorna

# Exemplo mais complexo(Um teste em uma entrevista para trabalhar com ciência de dados)

usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usuários que estão inativos no Twitter
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos2 = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos2)

# Resultado de ambas as formas
# [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'gal', 'tweets': []}]

# Combinar filter com Map
nomes = ['Alefe', 'Thaylane', 'Ayron']
# Criar uma lista contendo 'Sua instrutora é '+nome, desde que cada nome tenha menos de 5 caracter
# Usamos o map e o segundo parâmetro passamos a lista já filtrada
lista = list(map(lambda nome: f'A patroa é a {nome}', filter(lambda x: len(x) > 5, nomes)))
print(lista)
# ['A patroa é a Thaylane']








