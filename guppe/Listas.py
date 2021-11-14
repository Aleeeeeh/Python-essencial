"""
Listas
Listas em python funcionam como vetores, com a diferença de serem dinâmicos e também de podermos colocar
QUALQUER tipo de dado.

 - Dinâmico: Não possuem tamanho fixo; ou seja podemos criar a lista e simplesmente ir adicionando elementos;
 - Qualquer tipo de dado: Não possuem tipo de dado fixo;

 As listas em python são representadas por colchetes []

 Utilizando variáveis em listas
num = 1
num2 = 2
num3 = 3

numeros = [num, num2, num3]
print(numeros)

# Imaginar o indice como um circulo -1 será o último elemento -2 o penúltimo ...
cores = ['branco', 'verde', 'azul', 'verde']
print(cores[-1]) -> Verde

Como descobrir o indice dos valores em uma lista
lista = [1, 2, 3, 4, 5]
print(lista.index(4)) -> Indice 3

Revisao slice lista[inicio, fim, passo]
lista = [1, 2, 3, 4]
print(lista[1:]) -> Começando do indice 1 indo até o final
print(lista[:2]) -> Começando do zero indo até indice 2
print(lista[::]) -> Pegando todos os elementos da lista
print(lista[1::2] -> Começando  do indice 1 indo até final de 2 em 2

Soma, maximo, minimo e tamanho da lista
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

Desempacotando lista
lista = [1, 2 ,3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

Copiando listas Deep copy(cópia profunda), ou seja podemos adicionar novos valores na cópia, sem que a
original seja afetada
listagem = [1, 2, 3]
nova = listagem.copy()
nova.append(4)
print(nova) -> [1, 2, 3, 4], e listagem mantém 3 valores

Shallow copy, Cópia via atribuição, quando adicionamos um elemento a cópia o original também é
modificado, diferente do Deep copy.
listagem = [1, 2, 3, 4]
print(listagem)
nova = listagem
print(nova)
nova.append(5)
print(listagem)
print(nova)

"""
type([])  # Retorna tipo list

lista1 = [1, 5, 7, 9, 1, 6, 4]
lista2 = ['A', 'l', 'e', 'f', 'e']
lista3 = []
lista4 = list(range(11))
lista5 = list('Alefe Silva')

# Verificando se um número está contido na lista
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número')

# Podemos ordenar uma lista
lista1.sort()
print(lista1)

# Contagem de ocorrência de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Append adiciona um elemento por vez
lista1.append(23)
print(lista1)

#  Possivel apenas se adicionarmos uma nova lista dentro desta lista
lista1.append([15, 16, 17, 18, 19, 20])
print(lista1)

# Com extend inserimos vários valores dentro da lista
lista1.extend([96, 97, 98, 99, 100])
print(lista1)

# Inserindo novo elemento informando o indice que  queremos colocá-lo
lista1.insert(1, 'SHOW')
print(lista1)

# Concatenando listas, e tornando uma
lista1.extend(lista2)
print(lista1)

# Invertendo com reverse
lista2.reverse()
print(lista2)

# Copiando uma lista
lista6 = lista2.copy()
print(lista6)

# Verificar o tamanho da lista com len
print(len(lista6))

# .pop removemos ultimo elemento da lista, lista2.pop() -> Alef, podemos remover por indice colocando no
# parâmetro do .pop(2), lista2.clear() -> Remove todos os valores da lista

# Split tranformamos a string em uma lista, e separamos por espaço na lista
curso = 'Programação em python essencial'
curso = curso.split()
print(curso)

# Convertendo um lista em uma string, usamos um espaço vazio para separar e string com join
lista7 = ['Programação', 'em', 'python', 'essencial']
cursolista = ' '.join(lista7)
print(cursolista)

# Percorrendo uma lista com For
for elemento in lista1:
    print(elemento)

# Percorrendo com While
carrinho = []
produto = ' '

while produto != 'sair':
    produto = input('Digite um produto ou digite "sair" para sair: ')
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

cores = ['branco', 'vermelho', 'azul', 'verde']

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerando indice com o valor utilizando o enumerate
for indice, cor in enumerate(cores):
    print(indice, cor)

# Recebendo números inteiros, e tranformando em uma lista
i = 0
lista = []
while i < 6:
    valor = int(input('Entre com valor: '))
    lista.append(int(valor))
    i += 1

print(lista)




