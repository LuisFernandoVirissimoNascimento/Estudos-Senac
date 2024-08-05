# 23. Altere o programa de cálculo dos números primos, informando, caso
# o número não seja primo, por quais número ele é divisível.

intie = int(input("Dite um número: "))

if intie > 1:
    for i in range(2, int(intie**0.5) + 1):
        if (intie % i) == 0:
            print(i)
            print(intie, "não é primo")
    else:
        print(intie, "é primo")
else:
    print(intie, "não é primo")