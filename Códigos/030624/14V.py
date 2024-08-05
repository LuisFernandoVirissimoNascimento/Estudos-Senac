# Contagem de Vogais:
# Escreva uma função que recebe uma string e conta quantas vogais (a, e, i, o, u) ela contém.

def contagemdevogais(texto):
    a = 0
    e = 0
    bi = 0
    o = 0
    u = 0
    for i in texto:
        if i == "a":
            a += 1
        elif i == "e":
            e += 1
        elif i == "i":
            bi += 1
        elif i == "o":
            o += 1
        elif i == "u":
            u += 1
        else:
            print(" ")
    print(f"a {a}, e {e}, i {bi}, o {o} e u {u}")

contagemdevogais("Yipeeeeee")
        
