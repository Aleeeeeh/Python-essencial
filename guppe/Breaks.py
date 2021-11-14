"""
Break

Utilizamos break para sair de loops de forma projetada.
"""
# Exemplo Simples

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
# Exemplo com while
while True:
    comando = input('Digite "sair" para SAIR: ')
    if comando == 'sair':
        break