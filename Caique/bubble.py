def bubble_sort(lista):
    lenghtLista = len(lista)
    for topInt in range(lenghtLista):
        for bottomInt in range(0, lenghtLista-topInt-1):
            if lista[bottomInt] > lista[bottomInt+1]:
                lista[bottomInt], lista[bottomInt+1] = lista[bottomInt+1], lista[bottomInt]
    return lista

numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
print("Lista ordenada:", bubble_sort(numeros))
