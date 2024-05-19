def busca_binaria(arr, valor):
    limite_inferior = 0 
    limite_superior = len(arr) - 1
    
    while limite_inferior <= limite_superior:
        posicao_meio = (limite_inferior + limite_superior) // 2
        chute = arr[posicao_meio]
        if chute == valor:
            return posicao_meio
        elif chute > valor:
            limite_superior = posicao_meio - 1
        else:
            limite_inferior = posicao_meio + 1
            
    return None

def busca_linear(arr, valor):
    for i, v in enumerate(arr):
        if v == valor:
            return i


valores = [1, 4, 5, 7, 8, 12, 15, 16, 17, 17, 18, 19, 21, 23, 25, 27, 47, 78, 887,1232]
print(busca_linear(valores, 12))