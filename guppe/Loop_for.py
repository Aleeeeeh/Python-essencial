"""
Loop For
Loop -> Estrutura de repetição
For -> Uma dessas estruturas

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Em java:
for(int i=0; i < limitador; i++){
    //Execução do loop
}
Em Python:
for item in iterarável:
    //Execução do loop

Iterar - fazer novamente, repetir, reiterar

# Para cada letra contida em nome
for letra in nome:
    print(letra)

# For com lista
for numero in lista:
    print(numero)

# For com range
for numero in range(1, 10):
    print(numero)

ENUMERATE, pega uma coleção de valores, e retorna um objeto enumerado, como nos exemplos abaixo:
nome = 'geek'
((0, 'g'), (1, 'e'), (2, 'e'), (3, 'k'))

Exemplo utilizando método items (Semelhante ao enumerate)
dicionario = {'a': 1, 'b':2, 'c':3}

Com items buscamos a chave em si e o valor, com Enumerate pegamos o número do indice e valor
for chave, valor in dicionario.items():
    print(f'chave:{chave} e valor:{valor}')
RESPOSTA: chave: a e valor:1, chave:b e valor:2 etc...

# Exemplo de repetição com range, colocando +1 ele vai até o último valor
qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'Resultado da soma {soma}')
"""

nome = 'Geek university'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos de tranformar em uma lista

# Podemos tambem coloca print(letra), colocasemos _ no lugar de indice estariamos ignorando
for indice, letra in enumerate(nome):
    print(nome[indice])

# Buscando o indice e o valor
for valor in enumerate(nome):
    print(valor)

# Senão quisermos que pule linha a cada letra usamos end= ''
for letra in nome:
    print(letra, end='')

# Caracter unicode site apps.timwhitlock
# Original: U+1F60D
# Modificado: U0001F60D Substituimos o + por 000

# Exibindo 3 filas, com emojis de um a 10
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
