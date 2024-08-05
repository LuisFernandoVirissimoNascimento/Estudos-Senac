# 6. Jogo de Palavras:
# Crie um jogo onde o usuário digita uma palavra e o programa verifica se ela está no dicionário. Se estiver, exiba seu significado.

dicionatie = {"Banana" : "Banana é uma banana", "1" : "um número ", "Explosão" : "Explosão grande e destrutiva sei la", "Guerra e Glória" : "O Que se deve adquirir"}

checagem = input("Qual palavra você quer checar ?\n")
if checagem in dicionatie:
    print(dicionatie[checagem])