"""
POO - Classes

Em POO, classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente, ao
criar classes estamos criando um tipo de dado, como por exemplo "Lâmpada", não existe esse tipo em linguagem
de programação nenhuma, porém ao criar uma classe e dar um type vemos que o tipo dela é exatamente o nome da classe
criada.

Imagine que você queira fazer um sistema para automatizar o controle das lampadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iriamos querer saberse a lâmpada
    é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela e etc.

    - Métodos(funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar
    no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente iriamos querer
    representar no nosso sistema é o de ligar e desligar a mesma.

OBS: Quando nomeamos nossas em classes em Python, por convenção utilizamos o nome com inicial em maiusculo. Se o nome
for composto, as iniciais de ambas as palavras em maiusculo, e tudo junto.

Uma classe comum que utilizamos por exemplo é o int(), que é uma classe interna da linguagem, e com isso vemos um dos
motivos de a escrevermos classes com inicial maiuscula, para identificar o que foi criado pelo próprio Dev e o que já
é nativo da linguagem, exemplo:

class Int:
    pass


Imaginando um código grande, quando encontrarmos um momento que está classe acima estiver sendo chamado, já iremos
entender que se trata de uma classe criada e não a interna da linguagem, logo o Dev já se atentará de entender o que
essa classe criada faz.

"""


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))
