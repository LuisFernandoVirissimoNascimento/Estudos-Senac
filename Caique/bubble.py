def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Exemplo de uso
numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
print("Lista ordenada:", bubble_sort(numeros))
