# 1. Contagem de Palavras:
# O Crie um programa que leia um texto e conte quantas vezes cada palavra aparece.
# Armazene as palavras e suas contagens em um dicionário.


texto = input("Qual texto você quer checar a quantia de palavras :\n")

listaTexto = texto.split()
bibionario = {}
for i in range(len(listaTexto)):
    if listaTexto[i] not in bibionario:
        bibionario[listaTexto[i]] = 1
    else:
        bibionario[listaTexto[i]] += 1


print(bibionario)