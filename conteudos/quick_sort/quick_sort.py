def quicksort(array):
    if len(array) < 2:
        return array 
    else:
        meio = len(array) // 2
        pivo = array[meio]
        
        menores = [i for i in array if i < pivo] 
        iguais = [i for i in array if i == pivo] 
        maiores = [i for i in array if i > pivo] 
        return quicksort(menores) + iguais + quicksort(maiores)
    
    

if __name__ == "__main__":
    print(quicksort(["a", "z", "q", "c", "m", "b"]))
    print (quicksort([0, 10, 7, 9, 4, 3, 6, 5, 2, 1, 8]))
    