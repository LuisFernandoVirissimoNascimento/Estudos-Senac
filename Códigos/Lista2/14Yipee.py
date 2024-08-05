# 15. Faça um programa que peça 10 números inteiros, calcule e mostre a
# quantidade de números pares e a quantidade de números ímpares. 

bibaboboh = [int(input("give me : ")) for i in range(10)]
parparap = 0
imparaprar = 0
for i in bibaboboh:
    if i % 2 == 0:
        parparap += 1
    else :
        imparaprar += 1

print("par",parparap)
print("impar",imparaprar)
