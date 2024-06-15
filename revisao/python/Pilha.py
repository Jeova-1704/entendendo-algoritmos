import numpy as np

class Pilha:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.topo = -1
        self.pilha = np.empty(capacidade, dtype=int)
        
    def empilhar(self, valor):
        if self.topo == self.capacidade-1:
            print("A pilha está cheia")
            return 
        self.topo += 1
        self.pilha[self.topo] = valor
    
    def desempilhar(self):
        if self.topo == -1:
            print("A pilha está vazia")
            return
        self.topo -= 1