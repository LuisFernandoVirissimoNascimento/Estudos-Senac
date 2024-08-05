# Quadrado de Hashtags:
# Faça um programa que peça um número inteiro positivo ‘n’ ao usuário e imprima um
# quadrado de lado ‘n’ preenchido com hashtags. Por exemplo, para n=4, o resultado seria:
# ####
# ####
# ####
# ####

def imfeelinghype(intie):
    yeah = ""
    for i in range(intie):
        yeah += "#"
    for i in range(intie):
        print(yeah)

imfeelinghype(10)