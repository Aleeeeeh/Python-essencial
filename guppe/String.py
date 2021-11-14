"""
String:
nome = 'Alefe Silva'
print(nome.split()) -> ['Alefe', 'Silva'] -> Transforma em uma lista

Acessar uma parte da string usando coceito de indices de vetor, Nome dessa operação é slice de string
nome = 'Alefe Silva'
print(nome[0:5]) -> Alefe -> Pegamos indice 4, porém temos de colocar uma a mais no caso indice 5
print(nome[6:11]) -> Silva

Pegando primeira ou segunda palavra diretamente
print(nome.split()[0]) -> Alefe
print(nome.split()[1]) -> Silva

Indo o primeiro ao último elemento e invertendo
nome = 'efelA'
print(nome.[::-1]) -> Alefe

Substitui letras
nome = 'Alefe'
print(nome.replace('A', 'B') -> 'BLEFE', porém se tivesse mais de uma letra 'a' seria modificado
"""