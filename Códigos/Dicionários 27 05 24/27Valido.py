# 27. Dicionário de Livros:
# Crie um dicionário com títulos de livros e seus autores. 
# Peça ao usuário para digitar um título e exiba o autor correspondente.

dicionatie = {"Funny red one" : "Funny Mustache Man", "Polianna" : "Dscp, não sei", "Bury the Light" : "Power"}

checagem = input("Qual Livro você quer checar ?\n")
if checagem in dicionatie:
    print(dicionatie[checagem])
