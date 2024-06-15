def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [a for a in arr if a < pivo]
        iguais = [b for b in arr if b == pivo]
        maiores = [c for c in arr if c > pivo]
        
        return quickSort(menores) + iguais + quickSort(maiores)
    
    
vetor = [1, 4, 2, 3, 6, 4, 3, 7, 8, 3, 2, 1, 6, 8, 9]
print(quickSort(vetor))
    