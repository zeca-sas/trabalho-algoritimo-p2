
numeros = [64, 25, 12, 22, 11]
def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]


selection_sort(numeros)
print("Lista ordenada:", numeros)