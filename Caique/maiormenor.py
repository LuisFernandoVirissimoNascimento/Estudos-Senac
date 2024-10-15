def maior_e_menor_numeros(lista):
    return max(lista), min(lista)

# Exemplo de uso
numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
maior, menor = maior_e_menor_numeros(numeros)
print(f"O maior número é {maior} e o menor é {menor}.")
