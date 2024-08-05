# 22. Faça um programa que peça um número inteiro e determine se ele é
# ou não um número primo. Um número primo é aquele que é divisível
# somente por ele mesmo e por 1

intie = int(input("Dite um número: "))

if intie > 1:
    for i in range(2, int(intie**0.5) + 1):
        if (intie % i) == 0:
            print(intie, "não é primo")
            break
    else:
        print(intie, "é primo")
else:
    print(intie, "não é primo")