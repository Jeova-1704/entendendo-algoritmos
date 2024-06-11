from Vetor import Vetor


def testes_inteiros():
    vetor_inteiros = Vetor(int)

    # Testando o método adicionar
    vetor_inteiros.adicionar(1)
    vetor_inteiros.adicionar(2)
    assert vetor_inteiros.obter_posicao(1) == 0
    assert vetor_inteiros.obter_posicao(2) == 1

    # Testando o método inserir
    vetor_inteiros.inserir(1, 3)
    assert vetor_inteiros.obter_posicao(3) == 1
    assert vetor_inteiros.obter_posicao(2) == 2

    # Testando o método tamanho
    assert vetor_inteiros.tamanho() == 3

    # Testando o método buscar_item
    assert vetor_inteiros.buscar_item(0) == 1

    # Testando o método contem
    assert vetor_inteiros.contem(3) == True
    assert vetor_inteiros.contem(4) == False

    # Testando o método remover_index
    vetor_inteiros.remover_index(0)
    assert vetor_inteiros.tamanho() == 2
    assert vetor_inteiros.obter_posicao(3) == 0

    # Testando o método remover_item
    vetor_inteiros.remover_item(2)
    assert vetor_inteiros.tamanho() == 1
    assert vetor_inteiros.obter_posicao(2) == -1  

    # Testando o método ultimo_index
    assert vetor_inteiros.ultimo_index(1) == -1
    assert vetor_inteiros.ultimo_index(3) == 0

    print("Todos os testes do vetor de inteiro passaram!")



if __name__ == "__main__":
    print("oi")