"""
Reduce

Obs: A partir do Python 3 a função reduce() não é mais uma função integrada (built-in). Agora temos que importar e
utilizar esta função apartir do módulo 'functools'.

Guido Van Rossun: Utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes um loop for
é mais legível.

A função reduce() recebe dois parâmaetros, uma função e a coleção a ser percorrida(reduce semelhante ao for)

reduce(funcao, colecao) -> O reduce pega a função e vai passando os dados contidos na coleção um a um, e com resultado
anterior ele vai repassando a função até chegar no resultado final.
"""
# Exemplos práticos (Utilizanda a função reduce para multiplicar todos os valores da coleção)

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y

# Função irá recebe 2 e 3 resultando em 6, vai pegar esse valor e multiplicar por 4 e assim até terminar a coleção
res = reduce(multi, dados)
print(res)

# Utilizando laço for
res = 1
for n in dados:
    res = res * n
    print(f"Valor atual: {res}")

print(res)


