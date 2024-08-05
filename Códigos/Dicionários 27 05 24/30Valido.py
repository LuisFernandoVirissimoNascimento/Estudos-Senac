# 30. Dicionário de Países e Capitais:
# Crie um dicionário com nomes de países e suas capitais. 
# Peça ao usuário para digitar o nome de um país e exiba sua capital.

dicionatie = {"Alemanhã" : "Krakenhouse", "Brasil" : "Campo Grande", "País" : "Capital"}

checagem = input("Qual país você quer checar ?\n")
if checagem in dicionatie:
    print(dicionatie[checagem])