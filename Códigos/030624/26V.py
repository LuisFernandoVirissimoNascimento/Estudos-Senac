# Cálculo de Média Harmônica:
# Calcule a média harmônica de um conjunto de números. A fórmula é: H=x11+x21+…+xn1n

def calcular_media_harmonica(numeros):
    soma_reciprocos = sum(1/x for x in numeros)
    media_harmonica = len(numeros) / soma_reciprocos
    return media_harmonica

# Exemplo de uso da função:
numeros = [2, 4, 8, 16]
media_harmonica = calcular_media_harmonica(numeros)
print("A média harmônica dos números é:", media_harmonica)
