# 21. Dicionário de Números Romanos:
# Crie um dicionário que relacione números inteiros com suas representações em algarismos romanos (por exemplo, 1 → ‘I’, 5 → ‘V’, etc.). 
# Peça ao usuário para digitar um número e exiba sua representação romana.

dicionatie = {"1" : "I", "5" : "V", "4" : "VI"}

checagem = input("Qual número você quer checar ?\n")
if checagem in dicionatie:
    print(dicionatie[checagem])