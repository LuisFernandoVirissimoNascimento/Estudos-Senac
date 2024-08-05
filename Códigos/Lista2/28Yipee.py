# 29. Faça um programa que calcule o valor total investido por um
# colecionador em sua coleção de CDs e o valor médio gasto em cada um
# deles. O usuário deverá informar a quantidade de CDs e o valor para em
# cada um. 
bah = 0.0
bih = 0.0
while True:
    intie = float(input("Qual o valor de cada cd, digite 0 se quiser acabar.\n "))
    if intie == 0:
        break
    elif intie >= 1:
        bih += 1
        bah += intie

bah /= bih
print(f"A Média do custo é {int(bah)} e a quantia de cds é {bih}")