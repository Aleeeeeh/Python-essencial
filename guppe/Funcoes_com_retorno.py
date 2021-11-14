"""
Funções com retorno

Exemplo de função sem retorno o print, e função que retorna por exemplo o pop(), que retorna um elemento
com sem o último valor.EX:
numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}') -> [1, 2]

OBS: Quando um função em python não retorna nenhum valor, o retorno é none
OBS: Funções python que retornam valores, devem retornar esse valores com a palavra reservada return

Exemplo de função, neste exemplo não está retornando apenas imprimindo, por isso quando armazenamos
em uma variável e imprimimos depois não retona nada

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()
print(f'Retorno: {ret}')

DETALHE: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos
passar a execução da função para outras funções.

Sobre a palavra reservada return:
 - Ela finaliza a função, ou seja, ela sai da execução da função;
 - Podemos ter em uma função diferentes returns;
 - Podemos em uma função retorna qualquer tipo de dados e até mesmo múltiplos valores;
"""


# Refatorando o código acima para que retorne


def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(f'Retorno: {ret}')
print(f'Retorno: {quadrado_de_7() + 1}')


# Utilizando o return nos dá muito mais flexibilidade


def diz_oi():
    return 'Oi '


alguem = 'Thaylane!'
print(diz_oi() + alguem)


# Exemplo dentro de uma função podemos ter diferentes retornos


def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


# Podemos retornar múltiplos valores, no exemplo desempacotamos a função, e mostramoss tambem que a função
# retorna uma tupla


def outra_funcao():
    return 1, 2, 3, 4


num1, num2, num3, num4 = outra_funcao()
print(outra_funcao())

print(num1, num2, num3, num4)
print(type(outra_funcao()))

# Função para jogar a moeda(gera um número pseudo-randômico entre 0 e 1)
from random import random


# Podemos utilizar essa lógica para fazer um jogo de pedra papel e tesousa :)


def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'


print(joga_moeda())
