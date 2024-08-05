# 14. Contagem de Caracteres: 14 e 8 é exatamente a mesma pergunta.
# Leia um texto e conte quantas vezes cada caractere (letras, números, símbolos) aparece. Armazene os caracteres e suas contagens em um dicionário.

texto = input("Qual texto você quer checar a quantia de letras :\n")

bibionario = {}
for i in texto:
    if i not in bibionario:
        bibionario[i] = 1
    else:
        bibionario[i] += 1


print(bibionario)