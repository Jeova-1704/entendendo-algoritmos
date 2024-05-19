import numpy as np 


class Fila:
    def __init__(self, capacidade, tipo) -> None:
        self.__tipo = tipo
        self.__capacidade = capacidade 
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=self.__tipo)
        
    def adiconar_elemento(self, valor):
        if self.__topo+1 < self.__capacidade:

            self.__topo += 1
            self.__valores[self.__topo] = valor
        else:
            raise Exception("Tamanho máximo alcançado")
        
    def remover_elemento(self):
        for c in range(0, self.__topo):
            self.__valores[c] = self.__valores[c+1]        
        self.__topo -= 1
        
    def size(self):
        return self.__topo + 1    
            
    def visualizar_fila(self):
        for c in range(0, self.__topo + 1):
            print(f"Posição: {c} | Valor: {self.__valores[c]}")
        
        


if __name__ == "__main__":
    
    fila = Fila(5, int)
    fila.adiconar_elemento(1)
    fila.adiconar_elemento(2)
    fila.adiconar_elemento(3)
    fila.adiconar_elemento(4)
    fila.adiconar_elemento(5)
    fila.visualizar_fila()
    fila.remover_elemento()
    print()
    fila.visualizar_fila()
    
    
    
    
    