"""
Módulo collections: Ordered dict

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.
Tem como objetivo garantir a ordem de inserção de dados, pois em um dicionário não é garantida.
"""

from collections import OrderedDict

# Diferença entre enumerate e items está no arquivo de loop, com orderdict está garantida a ordem de
# inserção dos dados

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3})
for chave, valor in dicionario.items():
    print(f'Chave:{chave} e valor:{valor}')

# Teste para verificarmos a diferença de um dicionario comum e um orderedDict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True, pois dicionário comum a ordem não importa

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # False, pois mesmo que os valores sejam iguais não está na mesma ordem
