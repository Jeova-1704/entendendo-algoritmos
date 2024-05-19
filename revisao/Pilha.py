import numpy as np


class Pilha:
    def __init__(self, capacidade, tipo):
        self.__capacidade = capacidade
        self.__tipo = tipo
        self.__topo = -1
        self.__tamanho = 0
        self.__valores = np.empty(self.__capacidade, dtype=self.__tipo)

    def adicionar_elemento(self, valor):
        if isinstance(valor, self.__tipo):
            if self.__tamanho < self.__capacidade:
                self.__topo += 1
                self.__tamanho += 1
                self.__valores[self.__topo] = valor
            else:
                raise Exception("Tamanho máximo alcançado")
        else:
            raise Exception(
                f"Apenas valores do tipo {self.__tipo} são permitidos, você tentou inserir um elemento do tipo {type(valor)}"
            )

    def remover_elemento(self):
        if self.__tamanho > 0:
            self.__topo -= 1
            self.__tamanho -= 1
        else:
            raise Exception("pilha vazia, impossivel remover elemento.")
        
    def size(self):
        return self.__tamanho
    
    def ver_topo(self):
        if self.__tamanho > 0:
            return self.__valores[self.__topo]
        else:
            raise Exception("pilha vazia, impossivel remover elemento.")

    def visualizar_pilha(self):
        for c in range(self.__topo, -1, -1):
            print(f"Posição: {c} | Valor: {self.__valores[c]}")


if __name__ == "__main__":
    pilha = Pilha(5, int)
    pilha.adicionar_elemento(1)
    pilha.adicionar_elemento(2)
    pilha.adicionar_elemento(3)
    pilha.adicionar_elemento(4)
    pilha.adicionar_elemento(5)
    pilha.visualizar_pilha()
    print()
    pilha.remover_elemento()
    pilha.remover_elemento()
    pilha.visualizar_pilha()
    print()
    pilha.adicionar_elemento(5)
    pilha.adicionar_elemento(5)
    pilha.visualizar_pilha()
    print()
    print(pilha.ver_topo())
