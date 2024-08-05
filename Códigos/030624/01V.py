# Hipotenusa de um Triângulo Retângulo:
# Crie um programa que recebe os dois lados menores de um triângulo retângulo e uma
# função retorna o valor da hipotenusa.
import math as mt
def hipotenusa(a,b):
    a = a * a
    b = b * b
    c = mt.sqrt(b + a)
    print(f"O Valor da hipotenusa é {c}")

hipotenusa(3,4)