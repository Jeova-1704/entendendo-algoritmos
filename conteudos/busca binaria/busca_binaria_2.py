def pesquisa_binaria(arr, valor):
    limite_inferior = 0
    limite_superior = len(arr) - 1
    
    while True:
        posicao_atual = (limite_inferior + limite_superior) // 2
        
        if arr[posicao_atual] == valor:
            return posicao_atual
        elif limite_inferior > limite_superior:
            return -1
        else:
            if arr[posicao_atual] < valor:
                limite_inferior = posicao_atual + 1
                
            else:
                limite_superior = posicao_atual -1
                
                
                
lista_pequena= [x for x in range(0, 100)]
lista_grande = [x for x in range(0, 10000000)]


print(pesquisa_binaria(lista_pequena, 73))
print(pesquisa_binaria(lista_grande, 73))
