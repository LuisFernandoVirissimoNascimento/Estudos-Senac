# Soma dos Números Pares:
# Escreva uma função que recebe um número inteiro positivo ‘n’ e retorna a soma de todos os números pares de 1 até ‘n’.

def somaPar(intie):
    listie = []
    while intie != 0:
        listie.append(intie)
        intie -= 1
    intie = 0
    for i in range(len(listie)):
        if listie[i] % 2 == 0:
            intie += listie[i]

    print(intie) 


inta = int(input("Me dê o número a somar os pares\n"))
somaPar(inta)