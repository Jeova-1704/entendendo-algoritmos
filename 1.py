def ordenar(array):
    n = len(array)
    for i in range(0, n):
        menorI = -1
        menorE = array[i]
        for j, v in enumerate(array):
            if j >= i:
                if menorE > v:
                    menorE = v
                    menorI = j
        if menorI >= 0:
            array[i], array[menorI] = array[menorI], array[i]
            
def ordenar2(lista):
    for i in range(len(lista)):
        menor = min(lista[i:])
        temp = lista[i]
        pos_menor = 0
        for j in range(len(lista)):
            if lista[j] == menor:
                pos_menor = j
        lista[pos_menor] = temp
        lista[i] = menor
    return lista


def ordenar3(arr):
    numeros_ordenados = 0 
    while numeros_ordenados <= len(arr):
        for pos in range(0,len(arr)-1):
            aux = arr[numeros_ordenados:]
            if arr[pos] == menor_func(aux):
                arr[numeros_ordenados],arr[pos]= arr[pos] , arr[numeros_ordenados]
                numeros_ordenados += 1
    return arr
    

def menor_func(arr):
    print(arr)
    menor = arr[0]
    for i in range(0,len(arr)-1):
        if arr[i] < menor:
            menor = arr[i]
            
    return menor
     

vetor = [2, 1, 4, 3, 1, 1, 1, 0, 3, 6, 8, 7, 4, 8, 9, 3]
ordenar3(vetor)
print(vetor)