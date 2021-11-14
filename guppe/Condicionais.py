"""
Estruturas condicionais
If (se), else(senao), elif(senao se)

"""
idade = int(input('Digite sua idade: '))

# Usando o and de forma simplificada, poderiamos fazer if idade > 18 and idade < 60:
if 18 <= idade < 60:
    print('Maior de Idade')
elif idade >= 60:
    print('terceira idade')
else:
    print('Menor de Idade')
