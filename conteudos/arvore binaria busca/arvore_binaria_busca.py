class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivamente(self.raiz, valor)

    def _inserir_recursivamente(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivamente(no.esquerda, valor)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivamente(no.direita, valor)
        else:
            pass

    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, no, valor):
        if no is None:
            return False
        elif no.valor == valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivamente(no.esquerda, valor)
        else:
            return self._buscar_recursivamente(no.direita, valor)


if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()
    arvore.inserir(10)
    arvore.inserir(5)
    arvore.inserir(15)
    arvore.inserir(3)
    arvore.inserir(7)

    print(arvore.buscar(7))    
    print(arvore.buscar(20)) 
