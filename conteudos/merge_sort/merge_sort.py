def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerdo = merge_sort(arr[:meio])
    direito = merge_sort(arr[meio:])
    return merge(esquerdo, direito)

def merge(esquerdo, direito):
    result = []
    i = j = 0
    while i < len(esquerdo) and j < len(direito):
        if esquerdo[i] < direito[j]:
            result.append(esquerdo[i])
            i += 1
        else:   
            result.append(direito[j])
            j += 1
    result.extend(esquerdo[i:])
    result.extend(direito[j:])
    return result

if __name__ == "__main__":
    numeros = [31, 41, 59, 26, 42, 58]
    print(merge_sort(numeros))
    
