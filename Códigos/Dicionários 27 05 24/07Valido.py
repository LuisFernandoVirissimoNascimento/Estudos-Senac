# 7. Dicionário de Sinônimos:
# Crie um dicionário com algumas palavras e seus sinônimos. 
# Peça ao usuário para digitar uma palavra e exiba seus sinônimos.

dicionatie = {"Banana" : "amarelo e longo, comida de mamaco e Banana", "1" : "um número, minha posição nesse mundo, a quantia de vezes que venci moonsoon ", "Explosão" : "Explosão grande e destrutiva sei la, BAKURETSU BAKURETSU LA LA LA, EXPLOOOOOOOOOOOOOOOSIOOOOOOOOOOOOOON e Best Girl !", "Guerra e Glória" : "O Que se deve adquirir, justiça, o ideal e aquilo que faz um homem"}

checagem = input("Qual palavra você quer checar ?\n")
if checagem in dicionatie:
    print(dicionatie[checagem])
