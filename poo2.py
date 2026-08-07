class Produto:
    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(self.nome, self.endereco)

produtos = []

def cadastrar_produto(nome, preco_unitario):
    nome = input("Digite o nome do produto: ")
    preco_unitario = float(input("Digite o preço unitário do produto: "))

    produto = {
        "nome" : nome,
        "preco_unitario" : preco_unitario
    }

    produtos.append(produto)

    



print ("""[1] - cadastrar produto
[2] - listar produtos
[3] - comprar produto
[4] - sair""")

opcao = int(input("digite a opcao desejada"))



# i = 0 

# while i!=4:
#     if i == 1:
         