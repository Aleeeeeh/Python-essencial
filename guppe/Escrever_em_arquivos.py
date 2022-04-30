"""
Escrevendo em arquivos

Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmor um arquivo para escrita, não podemos lê-lo, somente escrever nele.
Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.
Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError
Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido.

# Forma tradicional de escrita em arquivo (Não Pythônica)
arquivo = open('mais.txt', 'w')
arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')
arquivo.close()

# Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Mais Esta é a última linha.')

with open('novo.txt', 'w') as arquivo:
    arquivo.write("Geek \n" * 20)

"""
cont = 0
with open('novo.txt', 'w') as arquivo:
    arquivo.write("*** Comanda *** \n\n")
    while True:
        cont += 1
        entrada = input("Digite o prato ou 'sair' para sair: ")
        if entrada != 'sair':
            arquivo.write(f"Nº {cont} - {entrada} \n")
        else:
            break
















