class Produto:
    def __init__(self, codigo, descricao):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = 0
        self.__quantidade = 0

    def mudaEstoque(self, acrescimo):
        quantidade += acrescimo

    def imprimeProduto(self):
        print("Codigo: ", self.__codigo, "Descricao: ", self.__descricao, "Preço: ", self.__preco, "Quantidade: ", self.__quantidade)

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,preco):
        self.__preco = preco

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

class Livro(Produto):
    def __init__(self, autor, numeroPaginas, codigo, descricao, preco, quantidade):
        Produto .__init__ (codigo, descricao, preco, quantidade)
        self.__autor = autor
        self.__numeroPaginas = numeroPaginas

class PecaCarro(Produto):
    def __init__(self, tipoCarro, marca, codigo, descricao, preco, quantidade):
        Produto .__init__ (codigo, descricao, preco, quantidade)
        self.__tipoCarro = tipoCarro
        self.__marca = marca

class Alimenticio(Produto):
    def __init__(self, validade, codigo, descricao, preco, quantidade):
        Produto .__init__ (validade, codigo, descricao, preco, quantidade)
        self.__validade = validade

class main():
    livro = Livro("Pedro", 15, 1, "Harry potter", 30.5, 1)
    Peca = PecaCarro("Chevrolet chevette", "Chevrolet", 2, "Carro para Ruas", "10.000", "1")
    alimenticio = ("27/11", 3, "Maçã", 22.3, 5)

        
        
        
