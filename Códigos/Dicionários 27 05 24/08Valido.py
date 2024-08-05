# 8. Contagem de Letras:
# Leia um texto e conte quantas vezes cada letra aparece. 
# Armazene as letras e suas contagens em um dicionário.

texto = input("Qual texto você quer checar a quantia de letras :\n")

bibionario = {}
for i in texto:
    if i not in bibionario:
        bibionario[i] = 1
    else:
        bibionario[i] += 1


print(bibionario)