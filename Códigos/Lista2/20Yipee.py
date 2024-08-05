# 21. Altere o programa de cálculo do fatorial, permitindo ao usuário
# calcular o fatorial várias vezes e limitando o fatorial a números inteiros
# positivos e menores que 16.
while True:
    intie = int(input("Dite um número, menor que 16 e se quiser sair dita 0: "))
    if intie == 0:
        break
    elif intie <= 16:
        intia = intie
        for i in range(intie -1, 0, -1):
            intia *= i
            
        print(intia)
    else:
        print("Valor inválido")