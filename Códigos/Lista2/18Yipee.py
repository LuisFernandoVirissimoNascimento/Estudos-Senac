# 19. Faça um programa que, dado um conjunto de N números, determine
# o menor valor, o maior valor e a soma dos valores
listie = []
while True:
    intie = int(input("Digite números para adicionar a lista, caso queira parar digite 0.\n"))
    if intie == 0:
        break
    else:
        listie.append(intie)


print(min(listie),"Minimo")
print(max(listie),"Maximo")
print(sum(listie),"Soma")