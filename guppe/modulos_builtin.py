"""
Trabalhando com módulos Builtin (módulos integrados, que já vem instalados no python)
Vem instalados, porém para usar precisamos fazer um import, para não sobrecarregar o sistema, toda vez que realizarmos
uma instancia carregar tudo.

# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())

# Podemos importar duas ou mais funções especificas de um módulo

from random import randint as rdi, random as rdm
print(rdi(5, 89))
print(rdm())
"""
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))
