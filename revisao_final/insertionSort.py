def insertion(arr):
    n = len(arr)
    for c in range(1,n):
        chave = arr[c]
        j = c - 1
        
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
        
        
if __name__ == "__main__":
    numeros = [31, 41, 59, 26, 42, 58]
    insertion(numeros)
    print(numeros)
