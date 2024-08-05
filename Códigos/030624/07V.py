# Lançamento de Moedas:
# Faça um programa para lançar uma moeda. Quando chamamos uma função, ela deve
# retornar “cara” ou “coroa”. Em outra função, faça ‘n’ lançamentos de moedas (onde ‘n’ é o
# valor que o usuário quiser) e mostre a porcentagem de vezes que deu cara e coroa. O que tende a acontecer se você jogar a moeda 10, 100, 1000 ou um milhão de vezes?

import random as rd

def coin():
    bah = rd.randint(0,1)
    if bah == 0:
        return "cara"
    else:
        return "coroa"
    
def countcoins(amount):    
    caras = 0
    coroas = 0
    for i in range(amount):
        count = coin()
        if count == "cara":
            caras += 1
        else:
            coroas += 1
    print(f"A Quantidade de coroas foi {coroas} e caras foi {caras}")

countcoins(1000000)