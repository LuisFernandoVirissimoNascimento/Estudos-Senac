def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Exemplo de uso
numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {calcular_fatorial(numero)}.")
