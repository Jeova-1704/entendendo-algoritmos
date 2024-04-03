class Pilhas:
    def __init__(self) -> None:
        self.__pilha = list()
        
    def adiciona(self, item):
        self.__pilha.append(item)
        
    def pop(self):
        if self.isEmpty():
            raise Exception("A pilha está vazia.")
        ultimoIndex = self.__getUltimoElemento()
        return self.__pilha.pop(ultimoIndex)
        
    
    def peek(self):
        if self.isEmpty():
            raise Exception("A pilha está vazia.")
        ultimoIndex = self.__getUltimoElemento()
        return self.__pilha[ultimoIndex]
    
    def isEmpty(self):
        if(self.__pilha == []):
            return True
        return False;
    
    def size(self):
        return len(self.__pilha)
    
    def clear(self):
        self.__pilha = list()
    
    def __getUltimoElemento(self):
        return len(self.__pilha) - 1
    
    def __str__(self) -> str:
        return str(self.__pilha)