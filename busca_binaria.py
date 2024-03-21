def busca_binaria(arr, item):
    baixo = 0
    alto = len(arr) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = arr[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
        
    return None

lista_teste = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(busca_binaria(lista_teste, 5))
print(busca_binaria(lista_teste, -2))
print(busca_binaria(lista_teste, 19))
