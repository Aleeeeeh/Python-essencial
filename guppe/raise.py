"""
Tratanto erros com raise

raise -> Lança excessões

OBS: Raise não é um função, e sim uma palavra reservada como def ou qualquer outra em python.
Simplificando, pense em raise com sendo útil para que possamos criar nossas próprias excessões e mensagens de erro.

O raise assim como return finaliza a função, ou seja, nada mais acontece depois de chamada.
"""
# Exemplo (TypeError pois está passando valor do tipo errado, deveria ser String, e valueError pois o valor
# deveria ser algum da lista de cores.)


def colore(texto, cor):
    cores = ["verde", "amarelo", "azul", "branco"]
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f"A cor precisa ser uma entre {cores}")
    print(f"O texto {texto} será impresso na cor {cor}")


colore("Geek", "azul")



