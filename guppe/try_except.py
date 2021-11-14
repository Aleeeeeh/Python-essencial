"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer em nosso código. Previndo que o programa
pare de funcionar e o usuário recebe mensagens de erro inesperadas.

try:
    // Execução problemática
except:
    // O que deve ser feito caso de problema

"""
# Tratando erro de forma genérica (NÃO RECOMENDADO)

try:
    geek()
except:
    print("Deu algum problema !")

print("***************************************************")
# Tratanto erro específico

try:
    geek()
except NameError:
    print("Você está utilizando uma função inexistente !")


print("***************************************************")
# Em casos onde queremos capturar o texto e salvar em log de erros por exemplo
try:
    len(5)
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: {err}")


print("***************************************************")
# Podemos captar várias excessões de uma vez.
try:
    # geek()
    len(5)
except NameError as err:
    print("Deu erro de NameError")
except TypeError as errb:
    print("Deu erro de TypeError")


print("****************************************************")
# Exemplo na prática (


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as errq:
        return f"Erro chave inexistente {errq}"
    except TypeError as erry:
        return f"Erro no tipo informado {erry}"


dic = {"Nome": "Ayron Pietro"}

print(pega_valor(dic, "Nome"))





















