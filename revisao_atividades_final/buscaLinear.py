def buscaLinear(arr, valor): #O(1)
    for i in range(0, len(valor)): #O(n + 1)
        if arr[i] == valor: #O(n)
            return i #O(1)
    return -1 #O(1)

"""
O(1) + O(n + 1) + O(n) + O(1) + O(1) => O(n)
"""