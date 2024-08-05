# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre
# uma mensagem caso o valor seja inválido e continue pedindo até que o
# usuário informe um valor válido.
while True:
    butbut = int(input("Me de entre 0 e dez"))
    if butbut <= -1 or butbut >= 11:
        print(":(")
    else:
        break