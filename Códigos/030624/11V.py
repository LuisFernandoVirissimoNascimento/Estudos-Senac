# Soma dos Dígitos:
# Escreva uma função que recebe um número inteiro e retorna a soma de seus dígitos. 
# Por exemplo, se o número for 123, a função deve retornar 6 (1 + 2 + 3).

def somadosdigitos(stringie):
    bintie = 0
    for i in stringie:
        bintie += int(i)
    print(bintie)

stringa = input("Me dê número :\n")
somadosdigitos(stringa)


