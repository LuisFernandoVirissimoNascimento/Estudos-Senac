# 26. Faça um programa que peça para n pessoas a sua idade, ao final o
# programa devera verificar se a média de idade da turma varia entre 0 e
# 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada. 
bah = 0
bih = 0
while True:
    intie = int(input("Qual a idade a ser adicionada, digite 0 se quiser acabar.\n "))
    if intie == 0:
        break
    else:
        bih += 1
        bah += intie

bah /= bih
if bah <= 25:
    print("Jovem",bah)
elif bah >= 26 <=60:
    print("Adulto",bah)
elif bah >= 61:
    print("Idoso",bah)