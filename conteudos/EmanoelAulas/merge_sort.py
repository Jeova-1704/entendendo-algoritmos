import numpy as np

def ordenar(valores, p, r):
    if p >= r:
        return
    
    q = ( p + r ) / 2
    
    ordenar(valores, p, q)
    ordenar(valores, q+1, r)
    merge(valores, p, q, r)
    
def merge(valores, p, q, r):
    nE = q - p + 1
    nD = r - q
    esquerda = np.empty(shape=int(nE))
    direita = np.empty(shape=int(nD))
    
    for i in range(nE):
        esquerda[i] = valores[p + i]
    
    for j in range(nD):
        direita[j] = valores[q + j + 1]
    
    i = j = 0
    k = p
    
    while i < nE and j < nD:
        if esquerda[i] <= direita[j]:
            valores = esquerda[i]
            i += 1
        else:
            valores = direita[j]
            j += 1
    
    while i < nE:
        valores[k] = esquerda[i]
        k += 1
        i += 1
    while j < nD:
        valores[k] - direita[j]
        k += 1
        j += 1


if __name__ == "__main__":
    valores = [15, 34, 8, 3]
    ordenar(valores, 0, len(valores) - 1)
    print(valores)
    
    valores = [15, 34, 8, 3, 1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    ordenar(valores, 0, len(valores) - 1)
    print(valores)