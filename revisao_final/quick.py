def quickSort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    pivo = arr[meio]
    menores = [x for x in arr if x < pivo]
    iguais = [y for y in arr if y == pivo]
    maiores = [z for z in arr if z > pivo]
    
    return quickSort(menores) + iguais + quickSort(maiores)


if __name__ == "__main__":
    numeros = [31, 41, 59, 26, 42, 58]
    ordenados = quickSort(numeros)
    print(ordenados)
"""
O (N log (n))
pois, por mais que ele use do principio de dividir para conquistar que tem complexidade de O(log (N)) ele ainda percorre todo o vetor para encontar 
os menores, maiores e iguais elementos do meu vetor.
toda vez ele percorre o vetor completo O(n) para pegar o meior, menor e igual elementos e colocar eles em uma lista a parte e efeturar novamente o quick
nas listas dos maiores e menores, sempre divindo na metade que é log (n)
"""