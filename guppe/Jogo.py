"""
Game - Pedra Papel e tesoura
"""
print('Digite corretamente tudo em minusculo e BOM JOGO! ')

from random import random


def pedra_papel_tesoura():
    valor = random()
    if 0 >= valor <= 0.3:
        return 'pedra'
    elif 0.3 > valor <= 0.65:
        return 'papel'
    return 'tesoura'


while True:
    jogador = input('Escolha pedra, papel ou tesoura: ')
    if pedra_papel_tesoura() == 'pedra' and jogador == 'papel':
        print('Papel vence pedra, Parabens ao Jogador')
    elif pedra_papel_tesoura() == 'papel' and jogador == 'tesoura':
        print('Tesoura vence papel, Parabens ao Jogador')
    elif pedra_papel_tesoura() == 'tesoura' and jogador == 'pedra':
        print('Pedra vence tesoura, Parabens ao Jogador')
    elif jogador == 'pedra' and pedra_papel_tesoura() == 'papel':
        print('Papel vence pedra, a máquina te venceu! ')
    elif jogador == 'papel' and pedra_papel_tesoura() == 'tesoura':
        print('Tesoura vence papel, a máquina te venceu! ')
    elif jogador == 'tesoura' and pedra_papel_tesoura() == 'pedra':
        print('Pedra vence tesoura, a máquina te venceu! ')
    else:
        print('Valor inválido, verifique a escrita e digite tudo minusculo, BOM JOGO !')
    jogo = input('Digite "Y" para continuar ou ENTER para encerrar o game ! ')
    if jogo == 'n':
        break

