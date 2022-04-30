"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')
print(arquivo.read())

seek() -> A função seek() é utilizada para  movimentação do cursor pelo arquivo. Ela recebe um
parâmetro que indica onde queremos colocar o cursor.

Exemplo:
Geek university -> arquivo.seek(2) ->  ek university

Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

arquivo.readLine() -> Lê linha a linha.
arquivo.read(50) -> Limitando quantidade de caracteres a serem lidos.

Em resumo:
arquivo = open('texto.txt') -> Abre arquivo
arquivo.read() -> Manipula arquivo
arquivo.closed -> Verifica se arquivo está aberto ou fechado (False -> ABERTO / True -> FECHADO)
arquivo.close() -> Fecha arquivo
"""
# Movimentando o cursor com a função seek()
arquivo = open('texto.txt')

print(arquivo.read())
arquivo.seek(8)
print("*************************")
print(arquivo.read())
print(f"Status do arquivo (aberto/fechado)-> {arquivo.closed}")
arquivo.close()
print(f"Status do arquivo (aberto/fechado)-> {arquivo.closed}")




