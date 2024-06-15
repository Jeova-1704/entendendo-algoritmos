class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(valor, self.raiz)

    def _inserir(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir(valor, no_atual.direita)

    def in_order(self, no_atual):
        if no_atual is not None:
            self.in_order(no_atual.esquerda)
            print(no_atual.valor, end=' ')
            self.in_order(no_atual.direita)

    def pre_order(self, no_atual):
        if no_atual is not None:
            print(no_atual.valor, end=' ')
            self.pre_order(no_atual.esquerda)
            self.pre_order(no_atual.direita)

    def post_order(self, no_atual):
        if no_atual is not None:
            self.post_order(no_atual.esquerda)
            self.post_order(no_atual.direita)
            print(no_atual.valor, end=' ')
            
    def inverter(self):
        self._inverter(self.raiz)
        
    def _inverter(self, no_atual):
        if no_atual is not None:
            no_atual.esquerda, no_atual.direita = no_atual.direita, no_atual.esquerda
            self._inverter(no_atual.esquerda)
            self._inverter(no_atual.direita)

if __name__ == "__main__":
    arvore = ArvoreBinaria()
    arvore.inserir(5)
    arvore.inserir(3)
    arvore.inserir(7)
    arvore.inserir(2)
    arvore.inserir(4)
    arvore.inserir(6)
    arvore.inserir(8)

    print("\nPre-order Traversal:")
    arvore.pre_order(arvore.raiz)
    arvore.inverter()
    print("\nPre-order Traversal:")
    arvore.pre_order(arvore.raiz)
