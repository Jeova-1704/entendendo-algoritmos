class No:
    def __init__(self, valor) -> None:
        self.__valor = valor
        self.__proximo = None
        
    def get_valor(self):
        return self.__valor
    
    def get_proximo(self):
        return self.__proximo
    
    def set_proximo(self, proximo):
        self.__proximo = proximo
        

class ListaEncadeada:
    
    def __init__(self) -> None:
        self.__inicio = None
        self.__fim = None
        
    def inserir_final(self, valor):
        novo_elemento = No(valor)
        
        if (self.__inicio == None):
            self.__inicio = novo_elemento
            self.__fim = novo_elemento
            
        else:
            self.__fim.set_proximo(novo_elemento)
            self.__fim = novo_elemento
    
    def inserir_inicio(self, valor):
        novo_elemento = No(valor)
        
        if (self.__inicio == None):
            self.__inicio = novo_elemento
            self.__fim = novo_elemento
            
        else:
            novo_elemento.set_proximo(self.__inicio)
            self.__inicio = novo_elemento
            
    def inserir_ordenado(self, valor):
        novo_elemento = No(valor)
        
        if (self.__inicio is None):
            self.__inicio = novo_elemento
            self.__fim = novo_elemento
            return
            
        elif valor < self.__inicio.get_valor():
            novo_elemento.set_proximo(self.__inicio)
            self.__inicio = novo_elemento
            return

        else:
            atual = self.__inicio
            anterior = No(None)
            
            while (atual is not None and atual.get_valor() < valor):
                anterior = atual
                atual = atual.get_proximo()

            anterior.set_proximo(novo_elemento)
            novo_elemento.set_proximo(atual)
                
    def printar(self):
        atual = self.__inicio
        while (atual is not None):
            print(atual.get_valor(), end=" ")
            atual = atual.get_proximo()
            
            
        
if __name__ == "__main__":
    lista_encadeada = ListaEncadeada()
    
    lista_encadeada.inserir_ordenado(5)
    lista_encadeada.inserir_ordenado(3)
    lista_encadeada.inserir_ordenado(1)
    lista_encadeada.inserir_ordenado(2)
    lista_encadeada.inserir_ordenado(4)
    lista_encadeada.printar()