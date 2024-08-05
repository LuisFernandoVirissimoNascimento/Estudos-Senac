# 13. Dicionário de Cidades:
# Crie um dicionário com nomes de cidades e suas populações. 
# Peça ao usuário para digitar o nome de uma cidade e exiba sua população.

dicionatie = {"Campo grande" : 3, "São paulo" : 500, "Duo Marshmallow Kingdom" : 69, "Big Flying quad dragon" : 3000000000000000000}

checagem = input("Qual cidade você quer checar a população ?\n")
if checagem in dicionatie:
    print(dicionatie[checagem])
