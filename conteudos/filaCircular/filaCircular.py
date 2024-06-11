import numpy as np 


class FilaCircular:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__inicio = 0
        self.__final = -1
        self.__numeros_elementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=int)
        
    def inserir(self, valor):
        if self.__numeros_elementos == self.__capacidade:
            print("A fila está cheia")
            return
        
        if self.__final == self.__capacidade - 1:
            self.__final = -1
        
        self.__final += 1
        self.__valores[self.__final] = valor
        self.__numeros_elementos += 1
        
    
    def remover(self):
        if self.__numeros_elementos == self.__capacidade:
            print("Fila vazia")
            return 
        
        temp = self.__valores[self.__inicio]
        self.__inicio += 1
        if self.__inicio == self.__capacidade:
            self.inserir = 0
        self.__numeros_elementos -= 1
        return temp
    
    def primeiro(self):
        if self.__numeros_elementos == self.__capacidade:
            return -1
        return self.__valores[self.__inicio]

    def ver_elementos(self):
        for valor in self.__valores:
            print(valor)




fila = FilaCircular(5)
fila.primeiro()
fila.inserir(10)
fila.inserir(11)
fila.inserir(12)
fila.primeiro()