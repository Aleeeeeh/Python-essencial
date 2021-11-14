"""
Loop While

Bloco While será repetido enquanto a expressão for verdadeira

Saindo de loops com Break
Usamos break para sair do loop de forma projetada

"""
resposta = ''

while resposta != 'sim':
    resposta = input('Acabou Jéssica: ')

# Exemplo break
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saindo do loop')

# Exemplo break com while
while True:
    comando = input('Digite "sair" para sair: ')
    if comando == 'sair':
        break
