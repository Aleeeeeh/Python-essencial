"""
O bloco with

Passo para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O block with é utilizado para depois de abrirmos o arquivo e manipular, saindo do bloco with o arquivo já estará
fechada.
** Forma mais profissional que os desenvolvedor python usam para manipulação de arquivos.
"""
with open('texto.txt') as arquivos:
    print(f"Status do arquivo (aberto/fechado): {arquivos.closed}")
    arquivos.seek(8)
    print(arquivos.readline())

print(f"Status do arquivo (aberto/fechado): {arquivos.closed}")
