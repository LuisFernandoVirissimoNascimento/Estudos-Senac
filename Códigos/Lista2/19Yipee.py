# 20. Altere o programa anterior para que ele aceite apenas números entre
# 0 e 1000. 

listie = []
while True:
    intie = int(input("Digite números para adicionar a lista, caso queira parar digite 1001. Só números de 0 a 1000\n"))
    if intie == 1001:
        break
    elif intie >= 0 and intie <= 1000:
        listie.append(intie)
    else:
        print("Número inválido")


print(min(listie),"Minimo")
print(max(listie),"Maximo")
print(sum(listie),"Soma")