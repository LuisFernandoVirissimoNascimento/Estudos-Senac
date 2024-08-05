# Jogo de Par ou Ímpar:
# Escolha 0 para par ou 1 para ímpar. Em seguida, forneça um número. 
# Crie um programa que determine se a soma do número escolhido com um número aleatório é par ou ímpar.

# Escolha 0 ou 1.
# ???????????????????????????
# Forneça um número

# Determine se a soma do NÚMERO ESCOLHIDO com o número aleatório é par ou impar

# Pergunte um numero pro jogador

# gere um numero aleatório

# pergunte pro jogador, se é par ou impar. e revele o resultado depois que o jogador tentar advinhar.

import random as rd

def guessgame():
    intie = int(input("Escolha um número inteiro :\n"))

    bintie = rd.randint(1,23456789009767898768789)
    print(bintie)
    stringie = input("Advinhe se a soma do número que você deu com um número aleatório secreto é par ou impar !!\n")
    intie += bintie
    if stringie == "par":
        if intie % 2 == 0:
            print("Correto, é par !")
        else:
            print(":(")
    else:
        if intie % 2 != 0:
            print("Yipee é impar")
        else:
            print(":(")

guessgame()