# 12. Dicionário de Produtos:
# Crie um programa que simule um carrinho de compras. 
# O usuário pode adicionar produtos (com nome e preço) ao carrinho e, no final, exiba o total da compra.

produtos = {}
total = 0
while True:
    funçãoSolicitada = input("0 - Sair\n1 - Checar produtos\n2 - Adicionar produtos\n3 - Remover produto\n")
    match funçãoSolicitada:
        case "0":
            print("Sair")
            break
        case "1": # Checar produtos
            print(produtos)
            for i in produtos:
                total += produtos[i]
            print(f"Total : R${total}")                    
        case "2": # Adicionar produtos
            chave = input("Nome do produto:\n")
            valor = float(input("Preço do produto:\n"))
            produtos[chave] = valor
        case "3": # Remover produto
            chave = input("Nome do produto para remover:\n")
            del produtos[chave]
        case _:
            print("Valor Inválido.")