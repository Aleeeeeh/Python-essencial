"""
Dunder Name e Dunder Main
Dunder -> Double under -> dois underline

Dunder Name -> __name__
Dunder Main -> __main__

Em Python, se executarmos um módulo diretamente na linha de comando, internamente o python atribuirá à variável
__name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

No exemplo abaixo, importamos o módulo primeiro, e podemos notar que quando executamos o arquivo
diretamente ele vem como main, se executamos através de um import ele executa como nome do arquivo,
neste caso primeiro.

if __name__ == "__main__":
    print("Teste !!!")
else:
    print(f"Nome do __name__: {__name__}")

Com isso verificamos se o arquivo está sendo executado diretamente ou sendo chamado por outro arquivo, e assim
evitamos que o arquivo seja executado através de import.
"""
import primeiro




