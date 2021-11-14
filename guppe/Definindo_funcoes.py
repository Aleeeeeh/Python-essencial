"""
Definindo funções

 - Funções são pequenos trechos de códigos que realizam tarefas especificas.
 - Pode ou não receber entradas de dados e retornar saida de dados.

Algumas funções já usadas até o momento no curso(Funções integradas do python)
 - print()
 - len()
 - max()
 - min()
 - count()
 - entre outras

Função append já não existe para string (AttributeError)
nome = 'Alefe ferreira'
nome.append('da silva')
print(nome)

Em python a forma geral de definir funções é: (def - definição)
def nome da função (parametros de entrada):
    bloco da função

Onde:
Nome da função SEMPRE com letras minusculas, e se for composto separado por underline(Snake case).
Parâmetros de entradas são opcionais, se tendo mais de um separar por virgula.
Bloco de função é onde processamento da função acontece, neste bloco pode ter ou não o retorno da função.

"""
# Exemplo de utilização de funções
cores = ['verde', 'amarelo', 'azul', 'branco']
cores.append('roxo')
print(cores)


# Para que não precisa-se ficar implementando para printar algo na tela, ja foi criado e integrado
# as linguagens a função print. Isso faz parte de um principio chamado:
# DRY - Don't repeat Yourself - Não repita você mesmo / Não repita seu código

# Definindo a primeira função

def diz_oi():
    print('Oi!')


diz_oi()


# Exemplo 2
def cantar_parabens():
    print('Parabens para voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante !')


cantar_parabens()

# Repetir varias vezes no lugar de chamar a função varias vezes podemos colocar em loop
for n in range(5):
    diz_oi()

# Em python podemos criar uma variável do tipo de uma função e executar está função através da variável
# Nem todas as linguagem permite isso
cantar = cantar_parabens
cantar()
