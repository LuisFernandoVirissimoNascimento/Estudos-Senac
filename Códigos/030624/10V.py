# Fatorial:
# Crie um programa que recebe um número inteiro positivo ‘n’ e calcula o fatorial desse número. 
# O fatorial de ‘n’ é o produto de todos os números inteiros positivos de 1 até ‘n’.
# Por exemplo, 5!=5⋅4⋅3⋅2⋅1=120

# I guess make a list, that that fat ass int and put it in the list, then go ahead and slap a fat -1 on it and add it to the list again if not 0, then stop that if it 0.
# then iterate that list and multiply everythang.

def fatorial(intie):
    listie = []
    while intie != 0:
        listie.append(intie)
        intie -= 1
    intie = 1
    for i in range(len(listie)):
        intie *= listie[i]

    print(intie) 


inta = int(input("Me dê o número a receber o fatorial\n"))
fatorial(inta)

