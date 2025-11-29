class Produto:
    def __init__(self, codigo, descricao):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = 0
        self.__quantidade = 0

    def mudaEstoque(self, acrescimo):
        quantidade += acrescimo

    def imprimeProduto(self):
        print("Codigo: ", codigo, "Descricao: ", descricao, "Preço: ", preco, "Quantidade: ", quantidade)

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
    def __init__(self, autor, numeroPaginas):
        Produto .__init__ (validade, codigo, descricao, preco, quantidade)
        self.__autor = autor
        self.__numeroPaginas = numeroPaginas

class PecaCarro(Produto):
    def __init__(self, tipoCarro, marca):
        Produto .__init__ (validade, codigo, descricao, preco, quantidade)
        self.__tipoCarro = tipoCarro
        self.__marca = marca

class Alimenticio(Produto):
    def __init__(self, validade, codigo, descricao, preco, quantidade):
        Produto .__init__ (validade, codigo, descricao, preco, quantidade)
        self.__validade = validade
        
        
        