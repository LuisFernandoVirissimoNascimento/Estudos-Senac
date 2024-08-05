# 25. Faça um programa que calcule o mostre a média aritmética de N notas

intie = int(input("Quantas notas você deseja inserir? "))
total = 0

for i in range(intie):
    nota = float(input("Insira a nota {}: ".format(i+1)))
    total += nota

media = total / intie
print("A média das", intie, "notas é:", media)
