"""
Módulo collections - Counter (contador)

Collections -> High performance container Datetypes (Tipos de dados de contêiner de alta performance)
counter -> Recebe um iterável como parâmentro e cria um objeto do tipo collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.
A grosso modo nos traz a quantidade de cada elemento, em um texto por exemplo, quantas palavras "cafe"
possui, e assim por diante.

"""
# Utilizando counter, primeiro temos fazer a importação da biblioteca de collections

from collections import Counter

# Podemos utilizar qualquer iterável, neste exemplo usamos lista
lista = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 48, 49, 50]

# A resposta traz a quantidade de ocorrências que cada chave possui, temos 2 números 1, então seria 1:2
res = Counter(lista)
print(type(res))
print(res)

# Exemplo 2
print(Counter('Geek University'))

# Exemplo 3
texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido 
na internet sob o princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável​​,
que todos possam editar e melhorar. O projeto é definido pelos princípios fundadores. O conteúdo é 
disponibilizado sob a licença Creative Commons BY-SA e pode ser copiado e reutilizado sob a mesma
licença — mesmo para fins comerciais — desde que respeitando os termos e condições de uso."""

palavras = texto.split()  # -> Split tranformar em lista, separa por virgula as palavras
res = Counter(palavras)

print(type(res))
print(res)

# Encontrando as cinco palavras com mais ocorrências
print(res.most_common(5))

