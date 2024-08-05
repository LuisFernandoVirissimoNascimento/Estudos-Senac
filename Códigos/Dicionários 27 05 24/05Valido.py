# 5. Controle de Estoque:
# Crie um dicionário para controlar o estoque de produtos em uma loja. 
# Permita adicionar, remover e atualizar a quantidade de cada produto.


Estoque = {}
while True:
    funçãoSolicitada = input("0 - Sair\n1 - Checar Estoque\n2 - Adicionar estoque\n3 - Remover estoque\n")
    match funçãoSolicitada:
        case "0":
            print("Sair")
            break
        case "1": # Checar Estoque
            print(Estoque)
        case "2": # Adicionar Produtos
            chave = input("Nome do produto:\n")
            valor = input("Quantia do produto:\n")
            Estoque[chave] = valor
        case "3": # Remover Produto
            chave = input("Nome do produto para remover:\n")
            del Estoque[chave]
        case _:
            print("Valor Inválido.")