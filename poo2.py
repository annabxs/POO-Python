class Produto:
    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(self.nome, self.endereco)

produtos = []

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco_unitario = float(input("Digite o preço unitário do produto: "))
    p1 = Produto(nome, preco_unitario)
    produtos.append(p1)

def listar_produto():
    print("\n ===Informações===")
    for i in range(len(produtos)):
        produto = produtos[i]
        print("Índice: ",i + 1)
        print("Nome do produto: ", produto.nome, "\nPreço do produto: R$", produto.preco, "\n" )

def comprar_produto():
    num = int(input("Digite o índice do produto: "))
    qtd = int(input("Digite a quantidade de produtos que deseja comprar: "))
    indiceP = produtos[num - 1]
    preco = qtd * indiceP.preco
    print("\n O preço final da sua compra é: R$", preco, "\n")
    if preco >= 100:
        print("Desconto disponível! \n")
    else:
        print("Sem desconto.\n")



opcao = 0
while opcao!=4:
    print ("""[1] - cadastrar produto
    [2] - listar produtos
    [3] - comprar produto       
    [4] - sair""")

    opcao = int(input("\n Digite a opcao desejada: \n"))
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
