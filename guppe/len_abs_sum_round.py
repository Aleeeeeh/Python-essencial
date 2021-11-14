"""
Len, Abs, Sum, Round

# Len
Len() -> Retorna o tamanho de um iterável.

OBS: O que acontece por debaixo dos panos(print('Teste'.__len__()) -> Funções que começa e termina com dois underline
é chamado de Dunder.

# Abs
abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica seria o valor real sem o sinal.

# Round

round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for
informada retorna o inteiro mais próximo da entrada.
"""
# Exemplos len (Funciona com qualquer iterável)
print(len('geek university'))
print(len([1, 2, 3, 4, 5]))
print("--------------")

# Exemplos abs(Valor absoluto, ou seja nunca trará numero negativo)
print(abs(5))
print(abs(-5))
print(abs(-3.14))
print(abs(3.14))
print("----------")

# Exemplos Sum
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))  # Podemos setar o valor default no caso vem no segundo parâmetro
print("-------------")

# Exemplos Round
print(round(10.5))  # De 5 pra baixo não arredonda
print(round(10.6))  # Acima de 5 arrendonda pra cima
print(round(1.212121, 2))  # 1.21
print(round(1.2199999, 2))  # 1.22













