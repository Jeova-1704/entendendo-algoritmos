class NO:
    def __init__(self, valor):
        self.__valor = valor 
        self.__proximo = None
        
    def setProximo(self, proximo):
        self.__proximo = proximo

    def getValor(self):
        return self.__valor

    def getProximo(self):
        return self.__proximo
    
class ListaLigada:
    def __init__(self) -> None:
        self.inicio = None
        self.fim = None
        
    def inverterLista(self):
        anterior = None
        atual = self.inicio
        self.fim = self.inicio
        while atual is not None:
            proximo = atual.getProximo()
            atual.setProximo(anterior)
            anterior = atual 
            atual = proximo 
        self.inicio = anterior
