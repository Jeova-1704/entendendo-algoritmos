def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > chave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = chave
        
if __name__ == "__main__":
    numeros = [4, 1, 5, 2, 6, 3, 7, 10, 9, 8]
    insertion_sort(numeros)
    print(numeros)