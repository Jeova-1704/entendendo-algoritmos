import numpy as np


class VetorVazioException(Exception):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)


class VetorMaxCapacidadeException(Exception):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)


class VetorOrdenado:
    def __init__(self, capacidade, tipo) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.tipo = tipo
        self.valores = np.empty(self.capacidade, dtype=self.tipo)

    # O(n)
    def inserir(self, valor):

        if self.ultima_posicao == self.capacidade - 1:
            raise VetorMaxCapacidadeException("Capacidade maxima do vetor atingida")

        if self.ultima_posicao == -1:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisar(self, valor):
        if self.ultima_posicao == -1:
            print("O vetor esta vazio")

        for c in range(self.ultima_posicao + 1):
            if self.valores[c] == valor:
                return c
            if self.valores[c] > valor:
                return None

        return None

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == None:
            print("Valor não existe no vetor")
            return

        for c in range(posicao, self.ultima_posicao + 1):
            self.valores[c] = self.valores[c + 1]

        self.ultima_posicao -= 1

    #log(n)
    def pesquisa_binaria(self, valor):
        if self.ultima_posicao == -1:
            print("O vetor esta vazio")
            return

        inicio = 0
        fim = self.ultima_posicao
        
        while True:
            posicao_meio = (inicio + fim) // 2
            if self.valores[posicao_meio] == valor:
                return posicao_meio
            elif inicio > fim:
                return None
            else:
                if self.valores[posicao_meio] < valor:
                    inicio = posicao_meio + 1
                else:
                    fim = posicao_meio - 1
                    
    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, " - ", self.valores[i])


if __name__ == "__main__":
    vetor = VetorOrdenado(10, int)
    vetor.inserir(1)
    vetor.inserir(3)
    vetor.inserir(5)
    vetor.imprime()
    print()
    vetor.inserir(2)
    vetor.inserir(4)
    vetor.imprime()
    print(vetor.pesquisar(6))
    vetor.excluir(4)
    vetor.imprime()
