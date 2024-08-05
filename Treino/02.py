listaProdutos = ["Batata","Feijão"]
while True:
    print("1 - Verificar Estoque\n2 - Adicionar ao estoque\n3 - Remover do Estoque\n4 - Sair do Sistema")
    prompt = input("")
    if prompt == "1":
        print("============================")
        for i in listaProdutos:
            print(i)
        print("============================")
    elif prompt == "2":
        print("============================")
        nomeProduto = input("Qual o nome do produto que vai ser adicionado ?\n")
        confirm = input(f"O Nome do produto é {nomeProduto}\n1 - Adicionar\n2 - Não Adicionar\n")
        if confirm == "1":
            listaProdutos.append(nomeProduto)
        print("============================")
    elif prompt == "3":
        print("============================")
        for i in listaProdutos:
            print(i)
        while True:
            nomeProduto = input("Qual o nome do produto que vai ser removido ?\n")
            booli = False
            for i in listaProdutos:
                    if i == nomeProduto:
                        booli = True
            if booli == False:
                print("Produto não existente\n1 - Tentar novamente\n2 - Sair")
                confirm = input("")
                if confirm == "1":
                    print("")
                else:
                    break
            else:
                break
        if booli == False:
            pass
        else:
            confirm = input(f"O Nome do produto é {nomeProduto}\n1 - Remover\n2 - Não Remover\n")
            if confirm == "1":
                for i in listaProdutos:
                    if i == nomeProduto:
                        listaProdutos.remove(i)
            else:
                pass
        print("============================")        
    elif prompt == "4":
        print("============================")
        print("Saindo.")
        print("============================")
        break
    else:
        print("Input Inválido")