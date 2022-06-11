"""
Funções de maior grandeza - Higher order functions - HDF

O que isso significa ?

 - Quando uma linguagem de programação suporte HDF, indica que podemos ter funções que retornam outras funções
 como resultado ou mesmo que podemos passar funções com argumentos para outras funções, e até mesmo variáveis do
 tipo de funções nos nossos programas.

 OBS: Na seção de funções, nós utilizmamos isso.
"""
from random import choice
# Exemplo


def soma(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 3, soma))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(10, 2, dividir))

# Nested functions - Funções Aninhadas
# Em python podemos também ter funções dentro de funções, que são conhecidas por Nested functions ou também
# Inner Functions (Funções internas).
print()
print("******* Nested functions ***********")


def cumprimento(pessoa):
    def humor():
        return choice(("Eai ", "Suma daqui ", "Gosto muito de você "))

    return humor() + pessoa


print(cumprimento("Zezin"))
print(cumprimento("jão"))
print("--------------------------")


def facame_rir():
    def rir():
        return choice(("kkkkk", "hahahah", "hehehehe"))
    return rir


# Aqui estamos retornando a função, o que faz executar é chamar com ()
rindo = facame_rir()
print(rindo())

# Podemos acessar o escopo de funções mais


def facame_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(("kkkkkkkk", "hahahaha", "hehehee"))
        return f"{risada} {pessoa}"
    return dando_risada


rindoDnv = facame_rir_novamente("zé delivery")
print(rindoDnv())



