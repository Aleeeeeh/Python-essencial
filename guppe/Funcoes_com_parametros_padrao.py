"""
Funções com parâmetros padrão

 - Funções onde a passagem de parâmetro seja opcional;
Exemplo: print()

Por quê utilizar parâmetros com valor default ?

 - Nos permite ser mais flexiveis nas funções;
 - Evita erros com parâmetros incorretos;
 - Nos permite trabalhar com exemplos mais legiveis de código;

Podemos passar vários tipos de dados como:
 - Strings, numeros, floats, listas, tuplas, dicionários e até funções;

"""


# Função com parâmetro padrão, sendo na hora da execução opcional passar tal argumento, se colocarmos
# valores padrão em todos os parâmetros então fica opcional passar os argumentos


def exponcencial(numero, potencia=2):
    return numero ** potencia


print(exponcencial(3))
print(exponcencial(3, 3))


# Exemplo mais complexo


def mostra_informacao(nome='geek', instrutor=False):
    if nome == 'geek' and instrutor:
        return 'Bem vindo instrutor geek'
    elif nome == 'geek':
        return 'Eu pensei que você fosse o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(nome='Alefe'))


# Exemplo passando funções como parâmetros, no exemplo do mat(8, 2, subtracao)Não é comum em outras
# linguagens de programação


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 2))
print(mat(10, 2, subtracao))

# Escopo - Variáveis globais e locais, as variáveis globais são aquelas contidas dentro de um escopo
# e podem sobrescrever variáveis globais como no exemplo, e também é interessante saber que variáveis
# locais são reconhecidas apenas dentro do bloco onde foram declaradas
instrutor = 'Geek'


def diz_oi():
    instrutor = 'Alefe'
    return f'Oi {instrutor}'


# Ao tentarmos acessar a variável instrutor diretamente, não teremos acesso a local
print(instrutor)
print(diz_oi())


# Para utilizar uma variável global para atribui valor dentro uma função, fazemos da seguinte forma
total = 0


def incrementa():
    global total
    total = total + 4
    return total


print(incrementa())

# Funções declaradas dentro de funções, usamos nonlocal para apontar que queremos usar uma variável
# que não é local e nem global


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


print(fora())
