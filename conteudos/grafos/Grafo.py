class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def adicionar_aresta(self, vertice1, vertice2, peso=1):
        self.adicionar_vertice(vertice1)
        self.adicionar_vertice(vertice2)
        self.vertices[vertice1][vertice2] = peso
        #self.vertices[vertice2][vertice1] = peso  # Se for um grafo não direcionado, descomente esta linha

    def obter_vertices(self):
        return list(self.vertices.keys())

    def obter_arestas(self):
        arestas = []
        for vertice in self.vertices:
            for vizinho in self.vertices[vertice]:
                arestas.append((vertice, vizinho, self.vertices[vertice][vizinho]))
        return arestas

    def __str__(self):
        resultado = ""
        for vertice in self.vertices:
            resultado += str(vertice) + " -> " + str(self.vertices[vertice]) + "\n"
        return resultado
    
    def print(self):
        return str(self.vertices)
        



if __name__ == "__main__":
    grafo = Grafo()
    grafo.adicionar_aresta('A', 'B', 5)
    grafo.adicionar_aresta('A', 'C', 3)
    grafo.adicionar_aresta('B', 'C', 1)
    grafo.adicionar_aresta('B', 'D', 2)
    grafo.adicionar_aresta('C', 'D', 4)

    print("Vertices:", grafo.obter_vertices())
    print("Arestas:", grafo.obter_arestas())
    print("Representação do grafo:")
    print(grafo)
    print(grafo.print())
