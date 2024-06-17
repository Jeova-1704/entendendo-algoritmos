def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2 
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    return merge(esquerda, direita)


def merge(direito, esquerdo):
    resultado = []
    i = j = 0
    while i < len(esquerdo) and j < len(direito):
        if esquerdo[i] < direito[j]:
            resultado.append(esquerdo[i])
            i += 1
        else:
            resultado.append(direito[j])
            j += 1
    resultado.extend(esquerdo[i:])
    resultado.extend(direito[j:])
    return resultado


if __name__ == "__main__":
    numeros = [31, 41, 59, 26, 42, 58]
    print(merge_sort(numeros))
    