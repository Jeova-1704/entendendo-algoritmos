class No:
    def __init__(self, valor) -> None:
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
        
    def inserir(self, valor):
        novo_elemento = No(valor)
        if self.inicio is None:
            self.inicio = novo_elemento
            self.fim = novo_elemento
        else:
            self.fim.setProximo(novo_elemento)
            self.fim = novo_elemento
    
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
        
    
    
    
    def imprimir(self):
        atual = self.inicio
        while atual is not None:
            print(atual.getValor())
            atual = atual.getProximo()


lista = ListaLigada()
lista.inserir(1)
lista.inserir(2)
lista.inserir(3)
lista.inserir(4)
lista.inserir(5)
lista.imprimir()
lista.inverterLista()
print("------------------")
lista.imprimir()
