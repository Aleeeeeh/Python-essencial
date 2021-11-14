"""
Mapas
Mapas em python são conhecidos como dicionários

"""
receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)

# Iterando sobre dicionários
for chave in receita:
    print(chave)

# Pegando só a chave usando método do python
print(receita.keys())

# Pegando apenas o valores tambem de forma pythonica
print(receita.values())

# Pegando apenas o valor
for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} recebi: {receita[chave]} reais')

# Desempacotamento de dicionários, exibe uma lista com três tuplas contendo chave e valor cada uma
print(receita.items())

# Soma, valor maximo, valor minimo, tamanho
print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))