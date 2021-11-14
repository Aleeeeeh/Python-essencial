""""
Try/ Except/ Else/ Finally

Dica de quando e onde tratar o código:

TODA ENTRADA DEVE SER TRATADA(A função do usuário é destruir seu sistema rsrs)

# ELSE -> É executado quando não ocorre o erro
num = 0
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto")
else:
    print(f"Voce digitou: {num}")
finally:
    print("Executando o finally")

# O finally, geralmente é utilizado para fechar ou desalocar recursos.Ex: Quando abrimos uma conexão com banco de dados
# para consulta etc... e sempre temos de fechar essa conexão, ou até mesmo pra fechar um arquivo que abrimos para
# leitura ou para escrita.

# Podemos criar um semi-genérico, exemplo:

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um erro: {err}"
"""
# Exemplo mais complexo


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Informe um valor numérico"
    except ZeroDivisionError:
        return "Nenhum número é divisivel por zero"


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print(dividir(num1, num2))







