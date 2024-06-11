import numpy as np

class FilaCircular:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.numeros_elementos = 0
        self.fila = np.empty(self.capacidade, dtype=int)
    
    def __fila_vazia(self):
        return self.numeros_elementos == 0
    
    def __fila_cheia(self):
        return self.numeros_elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__fila_cheia:
            print("A fil está cheia")
            return 
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.fila[self.final] = valor
        self.numeros_elementos += 1
        
    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila já está vazia")
            return
        
        temp = self.fila[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numeros_elementos -= 1
        return temp
        
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.fila[self.inicio]
        