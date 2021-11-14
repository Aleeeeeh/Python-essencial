"""
Conjuntos
 - Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoria dos conjuntos
 da matemática.
 No python os conjuntos são chamados de sets.
 Dito isto, da mesma forma que na matemática, sets não possuem valores duplicados ou ordenados
 Elemento que não podem ser acessado pelo indice, ou seja, não são indexados

 Conjuntos são bons para utilizar quando precisamos armazenar elementos que não nos importamos com a
 ordenação deles. Quando não precisamos nos preocupar com chaves, valores e items duplicados.

 A diferença entre conjuntos (sets) e dicionários:
  - Um dicionário tem chave/valor;
  - Um conjunto tem apenas um valor

Lista, tuplas, strings etc...para convertemos para conjuntos é simples
lista = [1, 2, 3, 4]
print(set(lista))

 - Soma, minimo, maximo, tamanho da mesmo forma que listas
 s = {1, 2, 3}
 print(sum(s)) -> 6

"""
# Forma 1, repare que ele não exibe os números repetidos
s = set({1, 2, 3, 4, 5, 3, 2, 4, 10})
print(s)
print(type(s))

# Forma 2 mais comum (Lembrando que são conjuntos pelo fato de haver apenas valores)
s = {1, 2, 3, 4, 5, 6}
print(s)
print(type(s))

# Comparação deas coleções em python, lista e tuplas aceitam duplicações, dicionários e sets desconsidera
# com isso no final ficam com número de chaves ou valores menores

lista = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = (1, 2, 2, 3, 3, 4, 5, 6, 7, 8)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionarios = {}.fromkeys([1, 2, 2, 3, 3, 4, 5, 6, 7, 8], 'dict')
print(f'Dicionario: {dicionarios} com {len(dicionarios)} elementos')

conjuntos = {1, 2, 2, 3, 3, 4, 5, 6, 7, 8}
print(f'Conjuntos: {conjuntos} com {len(conjuntos)} elementos')

# Usos interessantes de sets(Visitantes vierem de tais cidades, visando que tem pessoas que vieram do mesmo
# lugar, com o set podemos filtrar e saber quantas cidades são
cidades = ['sao paulo', 'belo horizonte', 'cuiaba', 'campo grande', 'sao paulo', 'belo horizonte']
print(cidades)
print(len(cidades))

# Set não permitir repetir valor, por isso conseguimos de fato ver quantas cidades são
quantidade_cidades = set(cidades)
print(quantidade_cidades)
print(len(quantidade_cidades))

# Adicionando elementos ao conjunto
s = {1, 2, 3}
s.add(4)
print(s)

# Removendo elementos do conjunto
s.remove(3)
print(s)

s.discard(2)
print(s)

# Deep copy e Shallow copy funciona da mesma maneira que os demais
# Lembrete: Deep copy, quando modificamos a cópia não afeta o original, fazemos isso utilizando o copy
print('EXEMPLO DE DEEP COPY E SHALLOW COPY NOVAMENTE')
set = {1, 2, 3}
novo = set.copy()
novo.add(4)
print(set)
print(novo)

# Shallow copy
teste = {1, 2, 3}
novo = teste
novo.add(4)
print(teste)
print(novo)

# Para limpar todos o dados de um conjunto também usamos o clear

# Métodos matemáticos de conjuntos
# Utilizando Union que é da própria matemática para podermos unir os dois conjuntos, os mesmos alunos
# que estudam python e java não será repetido na exibição

estudantes_java = {'Alane', 'Ayron', 'Godofredo', 'Astolfo', 'Max'}
estudantes_python = {'Alefe', 'Thaylane', 'Alane', 'Ayron', 'Bob'}

# RECOMENDADO (CLAREZA)
uniao1 = estudantes_java.union(estudantes_python)
print(uniao1)

# Forma 2 usando o caractere pipe |
uniao2 = estudantes_java | estudantes_python
print(uniao2)

# Gerando APENAS estudantes que estão em ambos os cursos usando intersection também da matemática
ambos = estudantes_java.intersection(estudantes_python)
print(ambos)

# Forma 2 utilizando o &
ambos2 = estudantes_java & estudantes_python
print(ambos2)

# Gerando estudante que estão apenas em um curso
soPython = estudantes_python.difference(estudantes_java)
print(soPython)

soJava = estudantes_java.difference(estudantes_python)
print(soJava)