"""
Módulo random  o que são módulos ?

- Em python, módulos nada mais são do que outros arquivos em python.
- Módulo random -> Possui várias funções para geração de números reais pseudo-aleatório.(Pseudo ou seja pode repetir numero).

OBS: Ao realizar o import de todo módulo, todas as funções, atributos, classes, e propriedades que estiverem dentro do
módulo ficarão disponíveis(Ficarão em memória). Caso você saiba quais funções você precisa utilizar deste módulo, então
esta não seria a forma ideal de utilização.
Ex: Se formos usar a função random em especifico podemos chamar from random import random.

import random

print(random.random())
# Obs: Não confunda a função random com pacote random.

# Uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos
from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 Não é incluído

# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas da mega sena
for i in range(6):
    print(randint(1, 61), end=", ")  # 61 não conta

# Choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadasCPU = ["Pedra", "Papel", "Tesoura"]
print(choice(jogadasCPU))

# shuffle() -> Tem a função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas.pop())
"""






















