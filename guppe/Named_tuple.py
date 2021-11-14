"""
Módulo collections - Named tuple

Named tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e tambêm parâmetros.


"""
from collections import namedtuple

# Precisamos definir o nome e parâmetros, 1° forma
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3 (Forma preferida do instrutor)
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Quando criamos um namedTuple estamos criando um tipo e seus valores no exemplo, tipo cachorro e seus
# valores idade, raca e nome
ray = cachorro(idade=2, raca='Chow chow', nome='Ray')
print(ray)

# Acessando elementos do namedTuple
print(ray[1])

# Forma 2
print(ray.nome)



