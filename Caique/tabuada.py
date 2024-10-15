def mostrar_tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Exemplo de uso
numero = int(input("Digite um número para ver sua tabuada: "))
mostrar_tabuada(numero)
