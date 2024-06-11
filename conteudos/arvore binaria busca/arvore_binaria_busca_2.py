class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_no(self):
        print(self.valor)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo_no = No(valor)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self.__inserir_recursivamente(self.raiz, valor)

    def buscar(self, valor):
        return self.__buscar_valor_recursao(self.raiz, valor)
    
    def pre_ordem(self, no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)
            
    def em_ordem(self, no):
        if no != None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    def __buscar_valor_recursao(self, no, valor):
        if no is None:
            return False
        elif no.valor == valor:
            return True
        elif valor < no.valor:
            return self.__buscar_valor_recursao(no.esquerda, valor)
        else:
            return self.__buscar_valor_recursao(no.direita, valor)

    def __inserir_recursivamente(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.__inserir_recursivamente(no.esquerda, valor)

        if valor >= no.valor:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.__inserir_recursivamente(no.direita, valor)


if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()

    arvore.inserir(53)
    arvore.inserir(30)
    arvore.inserir(14)
    arvore.inserir(39)
    arvore.inserir(9)
    arvore.inserir(23)
    arvore.inserir(34)
    arvore.inserir(49)
    arvore.inserir(72)
    arvore.inserir(61)
    arvore.inserir(84)
    arvore.inserir(79)
    
    print("============================================")

    print(arvore.raiz.esquerda.valor)
    print(arvore.raiz.direita.valor)
    
    print("============================================")
    
    print(arvore.pre_ordem(arvore.raiz))
    
    print("============================================")
    
    print(arvore.em_ordem(arvore.raiz))
