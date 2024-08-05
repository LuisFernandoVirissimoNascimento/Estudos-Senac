# Cálculo de Potência:
# Crie uma função que recebe a base e o expoente e calcula a potência. Por exemplo, 23=8

def calcular_potencia(base, expoente):
    resultado = base ** expoente
    return resultado

base = 2
expoente = 3
potencia = calcular_potencia(base, expoente)
print(f"{base}^{expoente} = {potencia}")
