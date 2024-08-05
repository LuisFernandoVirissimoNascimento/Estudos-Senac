# 17. Dicionário de Filmes:
# Crie um dicionário com títulos de filmes e seus anos de lançamento. 
# Peça ao usuário para digitar um título e exiba o ano de lançamento.

dicionatie = {"The birth of a good man" : "12 11 2001", "Oppenheimer" : "24 12 2024", "Barbie girl" : "24 12 2024"}

checagem = input("Qual filme você quer checar a data de lançamento ?\n")
if checagem in dicionatie:
    print(dicionatie[checagem])