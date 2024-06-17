class No:
    def __init__(self, valor) -> None:
        self.valor = valor 
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self) -> None:
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
        if valor >= no.valor:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivamente(no.direita, valor)
        