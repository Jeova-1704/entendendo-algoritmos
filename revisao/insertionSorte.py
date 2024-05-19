def insertion_sort(arr):
    n = len(arr)
    for c in range(1, n):
        chave = arr[c]
        j = c - 1
        
        while j >= 0 and arr[j] > chave:
            arr[j+1] = arr[j]
            j = j - 1
        
        arr[j + 1] = chave
        
        
if __name__ == "__main__":
    vetor = [1, 3, 1, 5, 6, 3, 2, 6, 3, 2, 6, 7, 8, 98, 45, 2, 52, 6, 52, 4, 2, 5, 4, 3, 25, 2, 5, 42, 6, 65, 6, 5, 7, 6, 7, 6, 8, 7, 98, 9, 0, 0, 1, 45, 4, 6, 56, 5, 5]
    insertion_sort(vetor)
    print(vetor)