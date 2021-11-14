"""
Generator Expression

Tuple comprehension são generators.

** Utilizando list comprehesion
nomes2 = ['Carlos', 'Camila', 'César', 'Cassiano', 'Cristiane', 'Daniel']
verificaPrimeiraLetra = [nome[0] == 'C' for nome in nomes]
print(any(verificaPrimeiraLetra)) -> true pois existindo um dado verdadeiro é o suficiente
"""
# Poderiamos ter feito utilizando generators
nomes = ['Carlos', 'Camila', 'César', 'Cassiano', 'Cristiane', 'Daniel']

# List Comprehension
verificaPrimeiraLetra = [nome[0] == 'C' for nome in nomes]
print(type(verificaPrimeiraLetra))
print(verificaPrimeiraLetra)

# Generators
verificaPrimeiraLetra = (nome[0] == 'C' for nome in nomes)
print(type(verificaPrimeiraLetra))
print(tuple(verificaPrimeiraLetra))

# Mostra quantos bytes a string 'Geek'está ocupando em memória. Quanto maior a string, mais espaço ocupa.
from sys import getsizeof

print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92345668823))

print(getsizeof(True))

# Mostra que o desempenho utilizando generator para gerar listas é melhor, pois ocupa menos espaço em memória
from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

# Essa diferença é dada pois esses três primeiros já geram e alocam espaço em memória, já o generator expression
# gera apenas quando é chamado
print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')  # 4508 bytes
print(f'Set Comprehension: {set_comp} bytes')  # 16492 bytes
print(f'Dictionary Comprehension: {dic_comp} bytes')  # 20536 bytes
print(f'Generator Expression: {gen} bytes')  # 56 bytes (RECOMENDADO)

"""
** Eu posso iterar no Generator Expression? Sim! **

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
"""
