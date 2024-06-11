from Fila import Fila



def test_fila():
    # Inicializando a fila
    fila = Fila()

    # Testando o método is_empty()
    assert fila.is_empty() == True

    # Adicionando alguns elementos à fila
    fila.adiciona(1)
    fila.adiciona(2)
    fila.adiciona(3)

    # Testando o método is_empty() novamente
    assert fila.is_empty() == False

    # Testando o método tamanho()
    assert fila.tamanho() == 3

    # Testando o método primeiro_elemento()
    assert fila.primeiro_elemento() == 1

    # Testando o método remove()
    assert fila.remove() == 1
    assert fila.remove() == 2

    # Testando o método verifica_presenca()
    assert fila.verifica_presenca(2) == False
    assert fila.verifica_presenca(3) == True

    # Testando o método copia()
    copia_fila = fila.copia()
    assert copia_fila == [3]
    assert copia_fila is not fila

    # Testando o método clear()
    fila.clear()
    assert fila.is_empty() == True
    assert fila.tamanho() == 0

# Chamando a função de teste
test_fila()

# Se nenhum AssertionError ocorrer, isso significa que todos os testes passaram
print("Todos os testes passaram!")