class Fila:
    
    def __init__(self) -> None:
        self.__fila = []
    
    def is_empty(self) -> bool:
        return len(self.__fila) == 0
    
    def adiciona(self, item) -> None:
        self.__fila.append(item)
        
    def remove(self) -> any:
        if not self.is_empty():
            return self.__fila.pop(0)
        else:
            raise IndexError("A fila está vazia.")        
                    
    def tamanho(self) -> int:
        return len(self.__fila)
    
    def primeiro_elemento(self) -> any:
        if not self.is_empty():
            return self.__fila[0]
        else:
            raise IndexError("A fila está vazia.")   
    
    def clear(self) -> None:
        self.__fila = []
        
    def verifica_presenca(self, item) -> bool:
        return item in self.__fila
    
    def copia(self) -> list:
        return self.__fila.copy()
    