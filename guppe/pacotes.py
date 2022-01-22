"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do python, um pacote deveria conter dentro dele um arquivo chamado __init__.py

Nas versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas normalmente ainda é utilizado para
manter compatibilidade.

"""
from geek import geek1, geek2


print(geek1.pi)
print(geek1.funcao1(2, 8))
print("----------------")
print(geek2.imprime_texto())


