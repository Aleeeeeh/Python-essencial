"""
Utilizando Lambdas

Conhecidas por expressões lambdas, ou simplesmente lambdas, são funções sem nomes, ou seja, funções anônimas.
"""
# Função em python


def soma(x):
    return 3 * x + 1


print(soma(4))

# Expressão lambda(não tem nome, já recebe o parâmetro direto e depois da um retorno)
lambda x: 3 * x + 1

# Como usar ?
calc = lambda x: 3 * x + 1
print(calc(4))

# Exemplo de quando usar, strip retira espaços se houver do inicio e do fim
nome_completo = lambda nome, sobrenome: nome.strip().title()+" "+sobrenome.strip().title()
print(nome_completo("alefe", "silva"))

# Podemos ter nenhuma ou vários parâmetros em funções em python
amar = lambda: "Como não amar Python"
um = lambda x: 3 + x * 2
print(amar())
print(um(2))

# Ordenando lista pelo sobrenome
familia = ["Alefe silva", "Thaylane Vitória", "Ayron Pietro", "Alane Vitória"]
familia.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
print(familia)

# Função quadrática usada para trajetória de projeteis, foguetes, em games tiro etc...
# f(x) = a * x ** 2 + b * x  + c

# Definindo função


def gera_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


# Podemos passar o parâmetro do lambda assim
teste = gera_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

# Ou de forma direta
print(gera_funcao_quadratica(2, 3, -5)(2))




