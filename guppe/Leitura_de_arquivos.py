"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

mode r -> Modo de Leitura. r -> read() -> ler

"""
arquivo = open('texto.txt')
# print(arquivo) -> <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
# print(type(arquivo)) -> <class '_io.TextIOWrapper'>

# A Função read() lê todo o conteudo do arquivo
print(arquivo.read())

# Lembrando que ao ler arquivo, tratamos de uma string, ou seja, conseguimos manipular o conteudo dentro do txt
# como uma simples string, usando split nela por exemplo e criando uma lista.
