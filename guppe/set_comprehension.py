"""
Set comprehension
"""
# Exemplos
numeros = {num ** 2 for num in range(10)}
print(numeros)

# DESAFIO ! Fazer uma alteração na estrutura acima para gerar um dicionário
numeros2 = {num: num ** 2 for num in range(10)}
print(numeros2)

# Finalizando...Lembrando que em Conjuntos não se repete valor e não posui ordenação
escola = {letras for letras in "geek university"}
print(escola)

