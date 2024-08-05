# Conversão de Temperatura:
# Crie um programa que converte uma temperatura em graus Celsius para Fahrenheit. A fórmula de conversão é: F=59C+32
def temp(floatie):
    floatie *= 1.8
    floatie += 32

    print(f"A Conversão dessa temperatura para farenheirt é {floatie}")


floata = float(input("Me dê a temperatura em celsius\n"))
temp(floata)