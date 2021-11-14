"""
Debuggando com PDB

PDB -> Python Debugger

Vida de inseto -> Life's Bug ^^

# Existem formas mais profissionais de se fazer 'debug'. utilizando o debugger. Em python podemos fazer isso em
diferentes IDES, como Pycharm ou o PDB.

# Clicando na linha colocamos um breakpoint, ou seja um ponto de parada. E para executar clicar no icone do inseto
# ao lado do botão iniciar ou clicando com botão direito e escolhendo a opção Debug.
# Com o debugger ativo, podemos selecionar por exemplo a divisão, clicar com botão direito e selecionar a opção
# Add inline watch, onde nos mostra o cálulo e resultado.


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um erro: {err}"


print(dividir(4, 0))
"""
# Exemplo com o PDB
# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()


# Comandos básicos do PDB
# l (Listar onde estamos no código, apontando com uma seta)
# n (Próxima linha) -> Next
# p (imprime variável)
# c (Continua a execução - finaliza o debugging)

"""
import pdb

nome = "Alefe"
sobrenome = "Silva"
pdb.set_trace()  # import pdb; import pdb -> Podemos fazer dessa forma também
nome_completo = nome + '' + sobrenome
curso = "Programação em python essencial"
final = nome_completo + 'faz o curso' + curso
print(final)

"""
# Apartir do python 3.7 podemos utilizar o PDB sem a necessidade de importar, pois ela se tornou uma função
# integrada, assim utilizamos o breakpoint conforme exemplo abaixo.

nome = "Alefe"
sobrenome = "Silva"
breakpoint()
nome_completo = nome + '' + sobrenome
curso = "Programação em python essencial"
final = nome_completo + " faz o curso " + curso
print(final)

"""
# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# Como os nomes das variávels são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel
"""






