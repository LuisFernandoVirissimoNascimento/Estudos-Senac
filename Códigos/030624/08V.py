# Dado Aleatório:
# Crie um dado em C++. A função deve sortear um número aleatório de 1 até 6. Agora, faça
# com que o dado seja lançado 100 vezes, mil vezes e 1 milhão de vezes. Armazene o valor
# que ele forneceu em cada lançamento e mostre quantas vezes cada número foi sorteado.
# Compare os resultados com a estatística.

import random as rd

def dados(amount):        
    one = 0
    two = 0
    tre = 0
    fah = 0
    fiv = 0
    sex = 0
    for i in range(amount):
        bah = rd.randint(0,5)
        if bah == 0:
            one += 1
        elif bah == 1:
            two += 1
        elif bah == 2:
            tre += 1
        elif bah == 3:
            fah += 1
        elif bah == 4:
            fiv += 1
        else:
            sex += 1
    print(f"1 {one}, 2 {two}, 3 {tre}, 4 {fah}, 5 {fiv} e finalmente 6 {sex}")
dados(100)
dados(1000)
dados(10000)
dados(100000)