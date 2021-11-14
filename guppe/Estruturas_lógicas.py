"""
Estruturas lógicas: and(e), or(ou), not(não), is(é)

Operadores unários(Depende de apenas um valor):
 - not
Operadores binários(Depende de dois valores):
 - and, or, is

 Regras:
  and - Ambos os valores precisam ser True
  or - Pelo menos um dos valores deve ser True
  not - Valor booleano é invertido, se for True fica False e vice-versa

  Exemplo:
  ativo = True
  logado = False
if not ativo: (not ativo - false, cairá no else)
    print('Verifique seu email, e ative sua conta')
else:
    print('Bem vindo ao sistema')
==========================================================================
    Exemplo (is):
if ativo is True: (Se o ativo é True exiba a mensagem)
    print('Bem vindo ao sistema')

Temos algumas funções associadas ao is exemplo:
nome = 'Alefe'
nome.isupper() - Está em maiusculo ?
nome.istitle() - É um titulo ?
"""
nome = 'Godofredo'
ativo = True
logado = True

if ativo and logado:
    print(f'Bem vindo {nome}')
else:
    print(f'{nome} você precisa ativar sua conta, favor verifique seu email')

# Ativo é True:
print(ativo is True)
