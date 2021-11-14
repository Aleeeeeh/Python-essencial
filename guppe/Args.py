"""
Entendendo o *args

 - O *args é um parâmetro como outro qualquer, ou seja você poderá chamar de qualquer coisa, desde
que comece com asterisco.
O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma
tupla. Então desde já lembre-se tuplas são imutáveis.
A grosso modo o parâmetro *args nos permite entrar com infinitos valores de entrada como no exemplo
abaixo, colocando os valores em uma tupla.

"""
# Entendendo o *args


def teste(nome, sobrenome, *args):
    return nome, sobrenome, args


print(teste('Alefe', 'Silva', 1, 99, 7))


# Dentro do parâmetro de *args estiver contido thayla E ferreira exiba as boas vindas


def verifica_info(*args):
    if 'thayla' in args and 'ferreira' in args:
        return 'Seja bem vinda Thayla !'
    return 'Não conseguimos encontrar sua identidade'


print(verifica_info(2, 3, 4, 'thayla', True, 'ferreira'))
print(verifica_info(2, 3, 'thayla', 'comassim', 65, False))

# *args considera uma lista de valores como um único, para conseguirmos passar uma lista para parâmetro args, podemos por
# exemplo desenpacotar


def soma_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5]

# Mesma coisa de num1, num2, num3, num4, num5 = numeros, o asteristico serve para informar ao python que estamos passando
# como argumentos uma coleção de dados, logo ele irá desempacotar os elementos automaticamente
print(soma_numeros(*numeros))

