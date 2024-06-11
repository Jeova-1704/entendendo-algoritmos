class Vetor:
    
    def __init__(self, tipo) -> None:
        self.__lista = list()
        self.__tipo = tipo
    
    def adicionar(self, item):
        if isinstance(item, self.__tipo):
            self.__lista.append(item)
        else:
            raise TypeError(f"Tipo de dado não suportado. A lista aceita apenas dados do tipo: {str(self.__tipo)}")
    
    def inserir(self, posicao, item):
        if isinstance(item, self.__tipo):
            if posicao >= 0 and posicao <= len(self.__lista):
                self.__lista.insert(posicao, item)
        else:
            raise TypeError(f"Tipo de dado não suportado. A lista aceita apenas dados do tipo: {str(self.__tipo)}")
        
    def tamanho(self):
        return len(self.__lista)
    
    def buscar_item(self, posicao):
        if posicao>= 0 and posicao < len(self.__lista):
            return self.__lista[posicao]
        else:
            raise IndexError("Posição informada não existente na lista")
    
    def obter_posicao(self, item):
        for posicao, elemento in enumerate(self.__lista):
            if elemento == item:
                return posicao
        return -1

    def contem(self, item):
        return self.obter_posicao(item) >= 0
    
    def remover_index(self, posicao):
        if posicao >= 0 and posicao < len(self.__lista):
            self.__lista.pop(posicao)
            
    def remover_item(self, item):
        if item in self.__lista:
            index = self.__lista.index(item)
            self.remover_index(index)
        else:
            raise ItemNaoExiste("Impossivel remover o item, ele não existe em sua lista.")
        
    def ultimo_index(self, item):
        for c in range(len(self.__lista)-1, -1, -1):
            if self.__lista[c] == item:
                return c
        return -1

    def __str__(self) -> str:
        return str(self.__lista)
    

class ItemNaoExiste(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem