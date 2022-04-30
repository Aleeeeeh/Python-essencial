"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. (Temos o controle do cursor)

#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adicionado SEMPRE ao final do arquivo. Com o modo 'a', não controlamos o cursor.

http://docs.python.org/3/library/functions.html#open

# Exemplo x
try:
    with open('novo.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe')


# Exemplo a
with open('novo.txt', 'a') as arquivo:
    while True:
        entrada = input("Digite o prato ou 'sair' para sair: ")
        if entrada != 'sair':
            arquivo.write(f"Nº 4 - {entrada} \n")
        else:
            break

# Exemplo r+
with open('novo.txt', 'r+') as arquivo:
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(32)
    arquivo.write('Mais uma linha.\n')
"""
numeroComanda = 0

try:
    with open('novo.txt', "r") as leitura:
        txt = leitura.read()
        lista = txt.split("\n")
        ultimo_item = lista[-2]
        numeroComanda = int(ultimo_item[3])
except IndexError:
    print("Criando nova comanda ...")


with open('novo.txt', 'a') as arquivo:
    if numeroComanda > 1:
        print("Reabrindo comanda ...")
    else:
        arquivo.write("*** Comanda *** \n\n")

    while True:
        numeroComanda += 1

        entrada = input("Digite o prato ou 'e' para encerrar pedido: ")
        if entrada != 'e':
            arquivo.write(f"Nº {numeroComanda} - {entrada} \n")
        else:
            break




