"""
Listas aninhadas
 - Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamada de arrays;
    - Unidimensionais (arrays/vetores)
    - multidimensionais (matrizes)

Em python temos ass listas;
"""
# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3 (3 linhas e 3 colunas)
print(listas)
print(type(listas))  # Não deixa de ser uma lista

# Acessando os dados
print(listas[1][2])  # Primeiro indice é a lista, o segundo é a posição em que se encontra o valor na lista (6)
print(listas[0][1])  # 2

# Iterando com loops em uma lista aninhada (Basicamente fazer dois laços for)
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

# Gerando tabuleiro/matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Gerando jogadas para o jogo da velha
velha = [["X" if numero % 2 == 0 else "O" for numero in range(1, 4)]for valor in range(1, 4)]
print(velha)  # [['X', 'O', 'X', 'O'], ['X', 'O', 'X', 'O'], ['X', 'O', 'X', 'O'], ['X', 'O', 'X', 'O']]













