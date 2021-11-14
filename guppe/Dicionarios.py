"""
Dicionários
Em algumas linguagens de programção os dicionários em python, são conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor.
print(type({}))

OBS: Em dicionários não podemos ter chaves repetidas

Quando não encontramos o valor, é exibido o segundo parâmetro('Não encontrado'), sem esse segundo parâmetro
e utilizando o get, no lugar de keyError retorna none
paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguay'}
pais = paises.get('ru', 'Não encontrado') -> se por exemplo a busca fosse py, e nao 'ru' exibiria Paraguay
print(f'Pais: {pais}')

"""
# Forma mais comum para criação de dicionários
paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguay'}
print(paises)
print(type(paises))

# Forma 2 menos comum
paisees = dict(br='Brasil', eua='Estados unidos', py='Paraguay')
print(paisees)
print(type(paisees))

# Acessando elementos (Acessando via chave) -> Se não achar o valor retorna keyError
print(paises['br'])

# Acessando via Get (Recomendado)
print(paises.get('eua'))
print(paises.get('ru'))  # -> Quando não temos o valor, Como estamos via get acusa o none, e não exibe

# Percorrendo o dicionário
print('br' in paises)
print('ru' in paises)
print('Estados unidos' in paises)  # Tambem bem erro pois é valor e não chave

# Podemos utilizar qualquer tipo de dado(int, float, string, boolean) inclusive lista e tuplas como chaves
# dicionários (As Cordenadas das localidades são apenas exemplo), aqui usamos tuplas e string, como chave e
# valor, a vantagem da tupla na chave é que ela é imutável

localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (40.5236, 322,354): 'Escritório em nova iorque',
    (37.7749, 122.4194): 'Escritório em são paulo'
}

# Adicionando elementos no dicionário
receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)
receita['abril'] = 400
print(receita)

# 2° forma de adicionar elementos no dicionário, tambem podemos receita.update({'maio': 500})
novo_dado = {'maio': 500}
receita.update(novo_dado)
print(receita)

# Para atualizarmos é do mesmo jeito
receita['maio'] = 550
print(receita)

# Inclusive para o update
receita.update({'maio': 600})
print(receita)

# Removendo dados do dicionário(chave/valor)
receita.pop('mar')
print(receita)

# 2° forma de remover dados do dicionário
del receita['jan']
print(receita)

# Imagine um e-commerce onde temos um carrinho de compras no qual adicionamos produtos
# 1 - Poderiamos utilizar listas, porém teriamos que saber qual o indice da informação do produto
carrinho = []

produto1 = ['PlayStation4', 1, 2300.00]
produto2 = ['Fifa2020', 1, 220.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# 2 - Poderiamos utilizar tuplas, com mesmo porém das listas
produto1 = ('PlayStation4', 1, 2300.00)
produto2 = ('Fifa2020', 1, 220.00)

carrinho = (produto1, produto2)

print(carrinho)

# 3 - Poderiamos utilizar um Dicionário, dessa forma conseguimos identificar melhor cada produto, e podemos
# adicionar e remover
carrinho = []

produto1 = {'nome': 'PlayStation4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'Fifa2020', 'quantidade': 1, 'preco': 120.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Métodos de dicionários, d.clear() limpa dados do dicionario
# As cópias funcionam da mesma forma que listas, Deep copy usa o copy, quando adicionamos um valor na
# cópia não modifica o original, ao contrário do shallow copy, que é via atribuição se modificar a cópia
# o dicionário original também é afetado
d = dict(a=1, b=2, c=3)
print(d)
novo = d.copy()
print(novo)
novo['d'] = 4
print(novo)

# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

# Atribuindo um valor para todas as chaves
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# Cada valor do range é uma chave, e novo é o valor dessas chaves
veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

