"""
Any e All

all() -> Retorna true se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

any -> retorna true se qualquer elemento do iterável for verdadeiro, se o iterável estiver vazio retorna false.
"""
# Neste exemplo irá retorna false, pois 0 é false
lista = [0, 1, 2, 3, 4]
print(all(lista))

# Pode ser qualquer iterável, uma tupla por exemplo
tupla = (1, 2, 3, 4)
print(all(tupla))  # True, não tem o zero

# String
string = 'Geek'
print(all(string))  # True, até mesmo se for um iterável vazio

# Pega a primeira letra de cada nome e verifica se começa com C no caso vai dar true
nomes = ['Carlos', 'Camila', 'César', 'Cassiano', 'Cristiane']
verificaPrimeiraLetra = [nome[0] == 'C' for nome in nomes]
print(all(verificaPrimeiraLetra))

# Compara se as letras existem na string aeiou, vai dar True pois ainda assim irá retorna um array vazio
comparaString = [letra for letra in 'ksr' if letra in 'aeiou']
print(all(comparaString))

# True, pois existe valores true dentro da lista
listaNum = [0, 1, 2, 3, 4]
print(any(listaNum))

# False, pois todos os elementos do iterável é falso
listaNum2 = [False, [], {}, (), 0]
print(any(listaNum2))

# Verifica se todos nomes começam com C, irá dar verdadeiro pois existem nomes com C
nomes2 = ['Carlos', 'Camila', 'César', 'Cassiano', 'Cristiane', 'Daniel']
verificaPrimeiraLetra = [nome[0] == 'C' for nome in nomes]
print(any(verificaPrimeiraLetra))



















