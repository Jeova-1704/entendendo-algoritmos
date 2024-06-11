def busca_binaria(arr, n):
    inferior = 0
    superior = len(arr) - 1
    
    while (inferior <= superior):
        meio = (inferior + superior) // 2
        chute = arr[meio]
        
        if chute == n:
            return meio
        if chute < n:
            inferior = meio + 1
        if chute > n:
            superior = meio - 1
    
    return -1

lista = [1, 2, 3, 4, 5]
numero_procurado = 3
indice = busca_binaria(lista, numero_procurado)
print(indice)  

            
            
            
# [1, 2|, 3, 4]  3