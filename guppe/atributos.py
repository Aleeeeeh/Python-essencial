"""
Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;

# Atributos de instância: são atributos declarados dentro do método construtor.
OBS: Método construtor é um método especial utilizado para construção de um objeto.

Exemplo em java, de uma classe com atributos e a classe construtora:
public class Lampada(){
    private int voltangem;
    private String cor;
    private boolean ligada = False;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Classe equivalente porém em Python:
class Lampada:
    def __init__(self, voltagem, cor): # Este def é um método
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

OBS: Toda função contida dentro de uma classe é um método e não mais uma função.

O que é o self ?
Self é o objeto que está executando o método, podemos colocar qualquer outro nome como primeiro parâmetro, porém
por convenção utilizamo a palavra self.
"""
# Classes públicas


class Lampada:
    def __init__(self, voltagem, cor):  # Este def é um método
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


"""
Atributos públicos e privados -> Públicos acessamos de qualquer lugar, privado apenas dentro da própria classe.
Em python por convenção, ficou estabelecido que todo atributo de uma classe é público, ou seja, pode ser acessado
em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratato como privado, ou seja, que deve ser acessado/
utilizado somente dentro da própria classe onde está declarado, utiliza-se __duplo underscore no inicio de seu nome.
Isso é conhecido também como Name Mangling.

LEMBRETE: Isso é só pra demonstrar que queremos que os atributos sejam acessados apenas dentro da própria classe,
mas a linguagem em si não irá bloquear se quisermos acessar por fora.
"""
# Classes com atributos privados


class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.__email)


user = Acesso("ze@gmail.com", "123456")

user.mostra_email() # Acessando normalmente, pois o método está dentro da classe
# print(user.__senha)  # AtributeError
print(user._Acesso__senha)  # Temos acesso mas não deveria.(Name Mangling).

# Quando criamos instancias de uma classe, todas as instancias terão atributos.
user1 = Acesso("user1@gmail.com", 123456)
user2 = Acesso("user2@gmail.com", 7891011)

user1.mostra_email()
user2.mostra_email()

# Atributos de classe


class Produto:
    # Atributo de classe(Atributo estático em java)
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    # Self.id Nesse caso não precisamos colocar no construtor pois trata-se de uma coluna que iremos incrementar
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        self.contador = self.id


p1 = Produto("Playstion 5", "Video game", 5000)
p2 = Produto("Xbox series S", "Video game", 2500)
p3 = Produto("Arroz", "Mercearia", 10)

print(p1.valor)  # Possivel, mas forma incorreta de acessar um atributo de classe
print(p2.valor)

# Obs: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(Produto.imposto)

# Atributos dinâmicos -> Pode ser criado em tempo de execução.(Será exclusivo da instancia que o criou, isso no é comum)
# Exemplo atributo peso não existe na classe.
p3.peso = "5kg"
print(p2.__dict__)
print(p3.__dict__)

# Deletando atributos dinâmicamente
del p3.peso

print(p2.__dict__)
print(p3.__dict__)



























