import numpy as np 

class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade 
        self.cabeca = 0
        self.cauda = -1
        self.numero_elementos = 0
        self.fila = np.empty(shape=self.capacidade, dtype=int)
    
    def enfileirar(self, valor):
        if self.numero_elementos == self.capacidade:
            print("A fila está cheia")
            return
        if self.cauda == self.capacidade - 1:
            self.cauda = -1
        self.cauda += 1
        self.fila[self.cauda] = valor
        self.numero_elementos += 1
    
    def desenfileirar(self):
        if self.numero_elementos == 0:
            print("A fila está vazia")
            return
        temp = self.fila[self.cabeca]
        self.cabeca += 1
        if self.cabeca == self.capacidade:
            self.capacidade = 0
        self.numero_elementos -= 1
        return temp
