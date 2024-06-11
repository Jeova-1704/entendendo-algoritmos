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


class VetorTipoException(Exception):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)


class VetorNaoOrdenado:
    def __init__(self, capacidade, tipo) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.tipo = tipo
        self.valores = np.empty(self.capacidade, dtype=self.tipo)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            raise VetorVazioException("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, " - ", self.valores[i])

    # O(1)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            raise VetorMaxCapacidadeException("Capacidade maxima do vetor atingida")

        if not isinstance(valor, self.tipo):
            raise VetorTipoException(
                f"Tipo do valor não compativél com o tipo do vetor! Apenas elementos do tipo {self.tipo} são permitidos"
            )

        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return None

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)

        if posicao == None:
            return None

        else:
            for i in range(posicao, self.ultima_posicao - 1):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1


if __name__ == "__main__":
    vetor = VetorNaoOrdenado(5, int)
    vetor.insere(2)
    vetor.insere(3)
    vetor.insere(4)
    vetor.insere(5)
    vetor.insere(6)
    print(vetor.ultima_posicao)
    vetor.imprime()
    print(vetor.pesquisar(4))
    vetor.excluir(6)
    vetor.imprime()
    print(vetor.ultima_posicao)
