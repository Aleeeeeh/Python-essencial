"""
Escopo de variáveis
 - Variaveis globais são reconhecidas, ou seja, seu escopo compreende todo programa;
 - Variaveis locais são reconhecidas apenas no bloco onde foram declarada;
 Exemplo:
 numero = 2
 if numero > 10:
    novo = numero + 10
    print(novo)

Novo é uma variavel local, só ira funcionar se a condição for atendida, já número é global, podemos exibir o
valor print(numero) -> 2, normalmente.

Python é uma linguangem de tipagem dinâmica, ou seja, quando declararmos uma variável, não colocamos o seu tipo,
pois seu tipo é inferido ao atribuirmos o valor à mesma.

"""
