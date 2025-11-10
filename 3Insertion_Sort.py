#Considera o primeiro elemento da lista como já ordenado.
#Pega o próximo elemento e o insere na posição correta em relação aos anteriores
numeros = [10, 31, 23, 53, 6]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave


insertion_sort(numeros)
print(numeros)

