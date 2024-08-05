# 3. Agenda Telefônica:
# Crie um programa que permita adicionar, buscar e remover contatos de uma agenda telefônica usando um dicionário.
contatos = {}
while True:
    funçãoSolicitada = input("0 - Sair\n1 - Checar Contatos\n2 - Adicionar Contatos\n3 - Remover Contato\n")
    match funçãoSolicitada:
        case "0":
            print("Sair")
            break
        case "1": # Checar Contatos
            print(contatos)
        case "2": # Adicionar Contatos
            chave = input("Nome do contato:\n")
            valor = input("Número do contato:\n")
            contatos[chave] = valor
        case "3": # Remover Contato
            chave = input("Nome do contato para remover:\n")
            del contatos[chave]
        case _:
            print("Valor Inválido.")