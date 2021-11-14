"""
Tipo booleano - Criado por George Boole
Forma correta de escrita com as iniciais maiusculas
True or False

OU (or), é uma operação binária, ou seja, precisa de dois valores, Um ou outro deve ser verdadeiro:
True or True -> Verdadeiro
True or False -> Verdadeiro
False or True -> Verdadeiro
False or False -> Falso

E (and), tambem é uma operação binária, ambos valores devem ser verdadeiros
True and True -> Verdadeiro
True and False -> Falso
False and True -> Falso
False and False -> False
"""
# Fazendo negação (not), resultado será contrário se for true resultado é false:
ativo = False
print(not ativo)

logado = False

# Exemplo do (or):
print(ativo or logado)

#Exemplo do (and):
ligado = True
desligado = False
print(ligado and desligado)



