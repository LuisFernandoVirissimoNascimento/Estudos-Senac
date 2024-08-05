# Ordenação de Números:
# Implemente um algoritmo de ordenação (por exemplo, Bubble Sort, Selection Sort ou Quick
# Sort) para ordenar um vetor de números inteiros.

def bubble_sort(vetor):
    n = len(vetor)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                # Troca os elementos se estiverem fora de ordem
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

# Exemplo de uso da função:
vetor = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(vetor)
print("Vetor ordenado usando Bubble Sort:", vetor)
