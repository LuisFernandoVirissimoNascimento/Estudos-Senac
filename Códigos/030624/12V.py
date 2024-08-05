# Média Aritmética:
# Crie um programa que pede ao usuário para digitar uma sequência de números e, em seguida, calcula a média aritmética desses números.

def calcular_media():
    def calcular_media(numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)

    numeros = []
    while True:
        try:
            entrada = input("Digite um número (ou 's' para sair): ")
            if entrada.lower() == 's':
                break
            numeros.append(float(entrada))
        except ValueError:
            print("Por favor, digite um número válido.")

    media = calcular_media(numeros)
    print("A média dos números digitados é:", media)

calcular_media()