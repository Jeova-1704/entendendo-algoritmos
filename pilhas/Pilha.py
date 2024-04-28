import numpy as np


class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __valores_cheia(self):
        return self.__topo == self.__capacidade - 1

    def __valores_vazia(self):
        return self.__topo == -1

    def empilhar(self, valor):
        if self.__valores_cheia():
            print("A pilha está cheia")
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__valores_vazia():
            print("A pilha está vazia")
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__valores_vazia():
            return -1
        return self.__valores[self.__topo]

    def isEmpty(self):
        return self.__valores_vazia()

    def size(self):
        return self.__topo + 1

    def clear(self):
        self.__topo = -1

    def __str__(self) -> str:
        return str(self.__valores[: self.__topo + 1])
