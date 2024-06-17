def buscaBinaria(arr, valor):
    limiteInf = 0
    limiteSup = len(arr) - 1
    
    while (limiteInf <= limiteSup):
        meio = (limiteSup + limiteInf) // 2
        chute = arr[meio]
        if chute == valor:
            return meio
        elif chute < valor:
            limiteInf = meio + 1
        else:
            limiteSup = meio - 1
    
    return -1



vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(buscaBinaria(vetor, 9))