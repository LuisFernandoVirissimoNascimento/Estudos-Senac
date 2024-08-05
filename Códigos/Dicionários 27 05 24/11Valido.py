# 11. Contagem de Vogais:
# Leia um texto e conte quantas vezes cada vogal (a, e, i, o, u) aparece. 
# Armazene as vogais e suas contagens em um dicionário.

texto = input("Qual texto você quer checar a quantia de letras :\n")

bibionario = {}
for i in texto:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        if i not in bibionario:
            bibionario[i] = 1
        else:
            bibionario[i] += 1


print(bibionario)