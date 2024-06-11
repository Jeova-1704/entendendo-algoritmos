def busca_linear(arr, n):
    for c in range(0, len(arr)):
        if arr[c] == n:
            return c
    return -1
        
        
        
print(busca_linear([1, 2, 3], 1))