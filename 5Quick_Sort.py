#Ele escolhe um pivô e reorganiza a lista de modo que
#Todos os elementos menores que o pivô fiquem à esquerda

numeros = [10, 7, 8, 9, 1, 5]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
    
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)
    

ordenada = quick_sort(numeros)

print(ordenada)
