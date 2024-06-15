import numpy as np 

class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.proximo = None
    
    def getValor(self):
        return self.valor
    
    def getProximo(self):
        return self.proximo
    
    def setProximo(self, valor):
        self.proximo = valor
        
    
class ListaEncadeada:
    def __init__(self, capacidade) -> None:
        self.inicio = None
        self.fim = None
    
    def inserir(self, valor):
        novoValor = No(valor)
        if self.inicio is None:
            self.inicio = novoValor
            self.fim = novoValor
            return
        self.fim.setProximo(valor)
        self.fim = valor
    
    def remover(self, valor):
        atual = self.inicio
        anterior = None
        while atual is not None:
            if atual.getValor() == valor:
                if anterior is None:
                    self.inicio = atual.getProximo()
                    if self.inicio is None:
                        self.fim = None
                else:
                    anterior.setProximo(atual.getProximo())
                    if atual == self.fim:
                        self.fim = anterior
                return True
            anterior = atual
            atual = atual.getProximo()
    
            
            
            
        