"""
Criando sua própria versão de loop

Releembrando como funciona o for por de baixo dos panos:
    - Itarable -> it = iter(iteravel) -> retorna um iterator
    - Iterator -> next(it) -> retorna o resultado da iteração do elemento

Função simulando o for !
"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


nome = "Geek university"
numeros = [1, 2, 3, 4, 5]

meu_for(nome)
print("----------------")
meu_for(numeros)


