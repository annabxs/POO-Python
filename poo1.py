class Produto:
    def __init__(self,codigo,nome,quantidade,preco_unitario):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def Mostrar(self):
        return self.codigo, self.nome, self.quantidade, self.preco_unitario

p1 = Produto(2,"lapis",2,2)
print (p1.Mostrar())