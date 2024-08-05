# 27. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

bobobo = 0
yipeeee = 0
kralegal = 0

bintie = int(input("Quantos eleitores ?\n"))
while bobobo + yipeeee + kralegal < bintie:
    intie = int(input("Qual dos três candidatos quer votar senhor novo eleitor ? 0 - Sair, 1 - bobobo, 2 - yipeeee, 3 - o kra q vai concertar tudo de errado nesse pais\n"))
    if intie == 0:
        break
    elif intie == 1:
        bobobo += 1
    elif intie == 2:
        yipeeee += 1
    elif intie == 3:
        kralegal += 1
    else:
        print(":(")

print(f"Os votos de {bintie} eleitores foram distribuidos da seguinte maneira, bobobo = {bobobo} votos, yipee = {yipeeee} votos, e kra boda = {kralegal} votos.")