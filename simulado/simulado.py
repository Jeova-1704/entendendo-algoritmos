#Q1
"""
Considere o vetor A não ordenado, contendo n elementos. Implemente o algoritmo de busca linear, que varre o vetor linearmente em busca de um valor específico. Caso encontre o valor procurado, retorne o índice onde o valor se encontra. Caso o valor não exista, retorne -1.
"""
def busca_linear(arr, valor):
    for c in range(0, len(arr)):
        if arr[c] == valor:
            return c
    return -1


#Q2
"""
Analise a complexidade do pior caso do algoritmo de busca linear implementado por você na questão 1.
"""
def busca_linear2(arr, valor): 
    for c in range(0, len(arr)): # O(n) + 1
        if arr[c] == valor: # O(1) 
            return c # O(1)
    return -1 # O(1)
"""
O(n)+1 * O (1) * O (1) + O (1)
corta as contantes
O (N)
"""

#Q3
"""
Implemente um algortimo de busca binaria
"""
def busca_binaria(arr, n):
    ponteiro_inferior = 0 # O(1)
    ponteiro_superior = len(arr) - 1 # O(1)
    
    while ponteiro_inferior <= ponteiro_superior: # log (n)
        ponteiro_meio = (ponteiro_inferior + ponteiro_superior) // 2 # O(1)
        chave = arr[ponteiro_meio] # O(1)
        
        if chave == n: # O(1)
            return ponteiro_meio # O(1)
        elif chave < n: # O(1)
            ponteiro_inferior = ponteiro_meio + 1 # O(1)
        else:  # O(1)
            ponteiro_superior = ponteiro_meio - 1 # O(1)
            
    return -1
#Q4 
"""
Faça a analise de complexidade do algoritmo acima:
Log (n)
o algoritmo utiliza a tecnica que divide para conquistar, onde a cada interação do meu laço while ele vai diminundo na metade o tamanho do vetore e na metade a quantidade de interação, ex:
[1, 2, 3, 4, 5], 1
[1, 2, 3], 1
[1], 1
isso fica em forma de uma função log n
"""

#Q5
"""
A expressão “O tempo de execução de um algoritmo é pelo menos O(n2)” está correta? Explique.

Não está correta, pois quando falamos "é pelo menos", está se referindo a algo de no minimo O(n^2) e a notação big O ela analisa sempre o pior caso possível, ou seja, o caso que tem a maior quantidade de passos, o pior caso naquele algoritmo e não o minimo, a notação correta para essa analise seria a notação  Ω (ômega), onde ela analisa sempre o melhor (pelo menos \ minímo) caso possível.
"""

#Q6 
"""
Não, não pode ser uma max-heap. Uma max heap é uma estrutura de arvore binaria, onde o pai sempre é maior do que os seus filhos, ou seja, cada nó é maior do que cada elemento abaixo dele, já um vetor ordenado não pode ser uma max heap, vamos supor, um vetor do tipo: [1, 2, 3, 4, 5, 6, 7] em forma de uma max heap:
            1
           / \
          2   3
         / \ / \
        4  5 6  7
        
se analizarmos a seguinte estrutura acima ela não pode ser considerada, já que os nós não são maiores do que os filhos, é o oposto, os filhos são maiores do que os pais
 
concluindo: Um array ordenado em ordem crescente não é uma max-heap porque a propriedade fundamental de uma max-heap (onde cada nó é maior ou igual aos seus filhos) não é satisfeita.
"""

#Q7
"""
Considere uma fila que utiliza um vetor como estrutura básica de armazenamento. Considere que ela é uma fila circular, isto é, seus ponteiros de cabeça e cauda são atualizados independentemente e podem fazer o wrap-around. Implemente os métodos de inserção e remoção de elementos nesta fila.
"""
import numpy as np
class Fila:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.numero_elementos = 0
        self.fila = np.empty(self.capacidade, dtype=int)
        
    def enfileirar(self, valor):
        if self.numero_elementos == self.capacidade:
            print("a fila está cheia")
            return 
        if self.fim == self.capacidade -1:
            self.fim = -1
        self.fim += 1
        self.fila[self.final] = valor
        self.numero_elementos += 1
    
    def desenfileirar(self):
        if self.numero_elementos == 0:
            print ("A fila esta vazia")
            return 
        
        temp = self.fila[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.capacidade -= 1
        return temp
        




if __name__ == "__main__":
    vetor = [1, 2, 3, 4, 5]
    print(busca_binaria(vetor, 8))
    print(busca_binaria(vetor, 1))
    print(busca_binaria(vetor, 4))