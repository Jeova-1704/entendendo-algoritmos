import numpy as np

class Pilha:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.topo = -1
        self.pilha = np.empty(capacidade, dtype=int)
        
    def empilhar(self, valor):
        if self.topo == self.capacidade - 1:
            print("A pilha está cheia")
            return 
        self.topo += 1
        self.pilha[self.topo] = valor
    
    def desempilhar(self):
        if self.topo == -1:
            print("A pilha está vazia")
            return None
        valor = self.pilha[self.topo]
        self.topo -= 1
        return valor
    
    def pilha_vazia(self):
        return self.topo == -1
    
    def imprimir_pilha(self):
        if self.topo == -1:
            print("A pilha está vazia")
            return
        print("Pilha: ", end="")
        for i in range(self.topo + 1):
            print(self.pilha[i], end=" ")
        print()

def inverter_pilha(pilha):
    capacidade = pilha.capacidade
    pilha_invertida = Pilha(capacidade)
    
    while not pilha.pilha_vazia():
        pilha_invertida.empilhar(pilha.desempilhar())
    
    return pilha_invertida


