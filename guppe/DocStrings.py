"""
Documentando funções com Docstrings

Docstrings são textos entre aspas triplas explicando trechos de uma função, mas tambem quando usamos
o help(print)por exemplo a documentação que nos devolve é baseado na docstring
No exemplo da função abaixo, se formos no terminal python acessar nosso arquivo através de
from DocStrings import diz_oi e digitarmos:help(diz_oi), aquilo que digitamos será uma pequena
documentação descrevendo o que o trecho da função faz no exemplo abaixo.
Podemos acessar a documentação também utilizando a propriedade da linguagem print(diz_oi.__doc__)

"""
# Exemplo


def diz_oi():
    """Uma função simples que retorna a string oi"""
    return 'oi!'


# Quando criamos a função e os parâmetros, e abrimos aspas duplas logo abaixo já aparece um pedaço
# de documentação padrão


def exponencial(numero, potencia=2):
    """
    Função que eleva um número ao quadrado, ou a potência informada
    :param numero:Número que será elevado a potência
    :param potencia:Potência padrão do número, podendo ser modificada
    :return:Retorna cálculo de numero elevado a potência
    """
    return numero ** potencia




