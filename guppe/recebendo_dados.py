"""
Recebendo dados do usuário
input() -> Todo dado recebido pelo input é uma string
A string pode ser colocados de dentro do input('dado')
"""
# Exemplo de print antigo, versão 2.x
""" 
print('Qual é o seu nome:')
nome = input()
print('Seja bem vindo(a) %s' % nome)

print('Qual sua idade: ')
idade = input()

# Quando temos 2 ou mais variáveis colocar entre parênteses
print('O %s tem %s anos' % (nome, idade))
"""
# Exemplo print versão moderno 3.x
"""
print('Qual é o seu nome: ')
nome = input()
print('Qual é a sua idade: ')
idade = input()
print('O {0} tem {1} anos de idade'.format(nome,idade))
"""
# Exemplo mais atual versão 3.7 +-, colocando f na antes das aspas
print('Qual é o seu nome: ')
nome = input()
print(f'Seja bem vindo(a) {nome}')
print('Qual sua idade: ')
idade = input() # idade = int(input()) Cast pode ser feito direto
print(f'O {nome} tem {idade} anos de idade')
print(f'O {nome} nasceu em {2020 - int(idade)}') #cast - Conversão de um tipo de dado para o outro

