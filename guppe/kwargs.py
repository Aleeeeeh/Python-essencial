"""
** kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que
utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.
A grosso modo os **kwargs funciona apenas se dermos de entrada chave e valor ao contrário do *args que apenas um valor
já funcionava.

"""
# Exemplo, vendo que o **kwargs é um dicionário conseguimos iterar sobre ele, usando laço for chave e valor


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(a=1, alefe='vermelho', thaylane='azul', alane='preto', ayron='preto')


# Exemplo se temos aquele nome na chave, e se o valor é aquele e então exibir a mensagem


def cumprimento(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return f'Você recebeu um cumprimento pythônico geek !'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek !'
    return 'Não tenho certeza de quem você é ...'


print(cumprimento())
print(cumprimento(geek='python'))
print(cumprimento(geek='Oi'))
print(cumprimento(geek='especial'))

# Por ordem de parâmetros em funções 1° params obrigatórios, 2° *args, 3°params opcionais e por último **kwargs:


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(23, 'Alefe', 1, 9, 9, 7, texto='Deu certo')

# Desempacotar com Kwargs, semelhante a forma que foi feita no args mas agora com dois **


def mostra_nome(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {'nome': 'Alefe', 'sobrenome': 'Silva'}
print(mostra_nome(**nomes))

# A forma que desempacotamos args também server para listas, tuplas e conjuntos


def soma_numeros(a, b, c):
    print(a + b + c)


listas = [1, 2, 3]
tuplas = (1, 2, 3)
conjuntos = {1, 2, 3}
dicionarios = dict(a=1, b=2, c=3)

soma_numeros(*listas)
soma_numeros(*tuplas)
soma_numeros(*conjuntos)
soma_numeros(**dicionarios)
