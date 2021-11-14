"""
Módulos collections - Default Dict

Default dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar
um lambda pra isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar
uma chave que não existe, essa chave será criado e o valor default será atribuido.

OBS: Lambdas são funções sem nome, que pode ou não receber parâmetros de entrada e retornar valores.

"""

# Import da biblioteca
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em python Essencial'
print(dicionario)

# No dicionarios comum daria KeyError, neste caso irá criar essa chave com valor default
print(dicionario['outro'])
print(dicionario)
