import numpy as np

class Fila:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.numero_elementos = 0
        self.fila = np.empty(capacidade, dtype=int)
        
    def enfileirar(self, valor):
        if self.numero_elementos == self.capacidade:
            print("A fila já está cheia")
            return
        if self.final == self.capacidade -1:
            self.final = -1
        
        self.final +=1 
        self.fila[self.final] = valor
        self.numero_elementos += 1
        
    def desenfileirar(self):
        if self.numero_elementos == 0:
            print("A fila está vazia")
            return
        temp = self.fila[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp