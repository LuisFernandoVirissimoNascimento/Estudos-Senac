# Número Perfeito:
# Um número é dito ser perfeito quando ele é igual à soma de seus divisores. Por exemplo, o seis é perfeito, pois: 6=1+2+3.
# Crie um programa que pede um número ao usuário e diga se ele é perfeito ou não.


def checarSeEPerfeito(perfect):
    controle = 0
    numeroCrescendo = 0
    while True:
        if controle >= perfect+1:
            print("Não é perfeito")
            break
        numeroCrescendo += 1
        if perfect % numeroCrescendo == 0:
            print(numeroCrescendo)
            pass
        else:
            continue
        controle += numeroCrescendo
        if controle == perfect:
            print("é perfeito:",numeroCrescendo)
            break

checarSeEPerfeito(8589869046)