#importacao
import pprint
from database import *

#menu de opcoes
def menu ():
    print(""" 
        1 - Cadastrar produto
        2 - Consultar/Listar produtos
        3 - Deletar conta
        4 - Mudar informações de produto
        5 - Criar uma nova categoria
        6 - Mudar nome da categoria
        7 - Consultar/Listar as categorias
        8 - Mudar produto de categoria
        9 - Produtos de determinadas categorias
      """)


#comeco produtos

#funcao para cadastrar produtos
def cadastrar_produtos (produtos):
    id = len(produtos) +1
    descricao = input("Digite a descrição do produto: ")
    vendedor = input("Digite o vendedor: ")
    preco = float(input("Digite o preço do produto: "))
    categoria = input("Digite o ID da categoria: ")

    produtos.append(f" id: {id}, descrição: {descricao}, vendedor: {vendedor}, preço: {preco}, categoria: {categoria} ")
    print(produtos)

#funcao para ver produtos
def ver_produtos (produtos):
    pprint.pprint (produtos)   

#funcao para deletar produtos especificos
def deletar_produto(produtos):
    delete = int(input('Digite o id do produto que deseja apagar: '))
    for produto in produtos:
        if produto["id"] == delete:
            indice = delete -1
            del produtos[indice]
    pprint.pprint(produtos)
    print("Esse produto já foi deletado!")

#funcao para mudar informacoes do produto
def modificar_informacoes_produto(produtos):
    id = int(input('Digite o id do produto que deseja modificar: '))
    vendedor = input('Digite o novo vendedor: ')
    descricao = input('Digite a nova descrição: ')
    categoria = input('Digite o ID da categoria: ')
    preco = float(input('Digite o novo preço: '))
    for produto in produtos:
        if produto["id"] == id:
            produto["vendedor"] = vendedor
            produto["descricao"] = descricao
            produto["categoria"] = categoria
            produto["preco"] = preco
    print(produto)
    print("O produto já foi alterado!")

#funcao para visualizar cada produto em sua categoria
def produtos_de_cada_categoria(produtos: list):
    for i in range(len(categoria)):
        idp = 1091
        if (idp+i) == 1091:
            print("\nEletrônicos")
        elif (idp+i) == 1092:
            print("\nGarrafa")
        elif (idp+i) == 1093:
            print("\nPerfume")
        for p in produtos:
            if p["id_categoria"] == (idp+i):
                print(f'[{p["id"]}] - {p["descricao"]} R${p["preco"]} reais')
    
    
def mudar_de_categoria(produtos):
    id = int(input('Digite o id do produto que deseja modificar: '))
    id_categoria = int(input('Digite o ID da nova categoria: '))
    for produto in produtos:
            if produto["id"] == id:
                produto["id_categoria"] = id_categoria
            print(produto)
    for i in range(len(categoria)):
        idp = 1091
        if (idp+i) == 1091:
                print("\nEletrônicos")
        elif (idp+i) == 1092:
                print("\nGarrafa")
        elif (idp+i) == 1093:
                print("\nPerfume")
        for p in produtos:
            if p["id_categoria"] == (idp+i):
                print(f'[{p["id"]}] - {p["descricao"]} R${p["preco"]} reais')

#fim de produtos
    
#comeco de categorias
    
#funcao para cadastrar uma nova categoria
def cadastrar_categoria(categoria):
    id = 1093
    id  +=1
    nome = input("Digite o nome da categoria: ")

    categoria.append(f" id: {id}, nome: {nome} ")
    print(categoria)

#funcao para mudar informacoes da categoria
def modificar_informacoes_categoria(categoria):
    print(categoria)
    id = int(input('Digite o id do produto que deseja modificar: '))
    nome = input('Digite o novo nome: ')

    for informacao in categoria:
        if informacao["id"] == id:
            informacao["nome"] = nome

    print("A categoria já foi alterada!")
    print(categoria)

#funcao para mostrar as categorias
def mostrar_categorias(categoria):
    pprint.pprint(categoria)