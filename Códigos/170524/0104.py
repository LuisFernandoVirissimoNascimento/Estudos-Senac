lista = [int(input("Me dê 10 numeros, vou tirar o 8 se tiver. : ")) for i in range(10)]
listona = []
for i in range(10):
    if lista[i] == 8:
        continue
    listona.append(lista[i])

print(listona)