# 9. Dicionário de Cores:
# Crie um dicionário com nomes de cores e seus códigos hexadecimais. 
# Peça ao usuário para digitar o nome de uma cor e exiba seu código.

dicionatie = {"Laranja" : "#e28743", "Preto" : "#21130d", "Branco" : "#eeeee4", "Azul" : "#1e81b0"}

checagem = input("Qual palavra você quer checar ?\n")
if checagem in dicionatie:
    print(dicionatie[checagem])
