# Existência de um Triângulo:
# Crie um programa que recebe os três lados de um triângulo e passa esses valores para uma
# função que verifica se esse triângulo existe ou não. Para que um triângulo exista, cada lado
# deve ser maior que o módulo da subtração dos outros dois lados e menor que a soma dos
# outros dois lados.


def verificar_existencia_triangulo(a, b, c):   
    if (a < b + c) and (b < a + c) and (c < a + b):
        print("Esse triangulo existe")
    else:
        print("Esse triângulo não existe")


verificar_existencia_triangulo(60, 50, 700)
