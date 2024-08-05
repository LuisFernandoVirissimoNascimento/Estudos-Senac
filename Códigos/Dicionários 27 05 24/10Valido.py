# 10. Jogo de Adivinhação:
# Crie um dicionário com palavras e suas definições. 
# O programa deve escolher uma palavra aleatória e pedir ao usuário para adivinhar seu significado.
import random as rd
dicionatie = {"Laranja" : "#e28743", "Preto" : "#21130d", "Branco" : "#eeeee4", "Azul" : "#1e81b0"}
whichWord = rd.random(1,4)
match whichWord:
    case 1:
        resposta = input("Qual o hexcode da cor laranja ?")
        if resposta == dicionatie["Laranja"]:
            print("Yipee !")
        else:
            print(":(")
    case 2:
        resposta = input("Qual o hexcode da cor preto ?")
        if resposta == dicionatie["Preto"]:
            print("Yipee !")
        else:
            print(":(")
    case 3:
        resposta = input("Qual o hexcode da cor Branco ?")
        if resposta == dicionatie["Branco"]:
            print("Yipee !")
        else:
            print(":(")
    case 4:
        resposta = input("Qual o hexcode da cor Azul ?")
        if resposta == dicionatie["Azul"]:
            print("Yipee !")
        else:
            print(":(")
