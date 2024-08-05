# 23. Dicionário de CEPs:
# Crie um dicionário com nomes de cidades e seus CEPs. 
# Peça ao usuário para digitar o nome de uma cidade e exiba seu CEP.

dicionatie = {"Campo grande" : "7764535", "Corona" : "4534555", "Babobant" : "4353463634"}

checagem = input("Qual cep você quer checar ?\n")
if checagem in dicionatie:
    print(dicionatie[checagem])
