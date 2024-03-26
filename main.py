from database import produtos, categoria
from lib.funcoes import cadastrar_produtos, ver_produtos, deletar_produto, modificar_informacoes_produto, cadastrar_categoria, modificar_informacoes_categoria, menu, mostrar_categorias, produtos_de_cada_categoria, mudar_de_categoria

while True:
        menu()
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1: 
            cadastrar_produtos(produtos)

        elif opcao == 2: 
            ver_produtos(produtos)

        elif opcao == 3:
            deletar_produto(produtos)

        elif opcao == 4:
            modificar_informacoes_produto(produtos)

        elif opcao == 5: 
            cadastrar_categoria(categoria)

        elif opcao == 6:
            modificar_informacoes_categoria(categoria)

        elif opcao == 7:
            mostrar_categorias(categoria)

        elif opcao == 8:
            mudar_de_categoria(produtos)
            
        elif opcao == 9:
           produtos_de_cada_categoria(produtos)



        else:
                print('Porfavor selecione uma opção válida')
        
        break