"""
Funções com parâmetro (entrada)

 - São funções que recebem dados para serem processadas dentro da mesma;

"""
# Refatorando a função da aula de funções com retorno


def quadrado(numero):
    return numero * numero


print(quadrado(7))

# Refatorando a função cantar parabéns


def cantar_parabens(aniversariante):
    print('Parabens para voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante} !')


cantar_parabens('Alane')
# Funções podem ter n parâmetros de entrada, no exemplo iremos exibir varias vezes o nome


def exibir(num1, num2, nome):
    return(num1 + num2) * nome


print(exibir(5, 5, 'Ayron '))

# Diferença entre argumentos e parâmetro


def nomeCompleto(nome, sobrenome):
    return f'Nome completo é: {nome} {sobrenome}'


# Argumento está contido na hora do execução, ou seja, os dados passados.
print(nomeCompleto('Thaylane', 'Ferreira'))

# Argumentos nomeados (Key arguments) - Neste caso a ordem dos argumentos não importa
print(nomeCompleto(sobrenome='Ferreira', nome='Alefe'))


# Erros comuns na utilização do return, lembrando que o return finaliza a execução por isso, não
# deve ficar abaixo do if e sim do for como no exemplo


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))



