class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = []

    def adicionar_aresta(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.arestas.append((u, v))

    def calcular_informacoes(self):
        num_vertices = len(self.vertices)
        num_arestas = len(self.arestas)
        graus = [0] * num_vertices

        for u, v in self.arestas:
            graus[u - 1] += 1
            graus[v - 1] += 1

        grau_minimo = min(graus)
        grau_maximo = max(graus)
        grau_medio = sum(graus) / num_vertices

        graus.sort()
        mediana = graus[num_vertices // 2]

        return num_vertices, num_arestas, grau_minimo, grau_maximo, grau_medio, mediana

    def componentes_conexas(self):
        # Implementar aqui o algoritmo BFS ou DFS para encontrar as componentes conexas.
        pass

#    def vetorDeAjacencia(self):
#        vetor = np.array([])
#        for vertice in range (1, self.vertices):
#            vetor.concatenate(vetor)
#            for linha in self.arestas:
#                if str(vertice) in linha:
#        for linha in self.arestas:
            

    def ler_grafo(self, arquivo_entrada):
        with open(arquivo_entrada, 'r') as arquivo:
            num_vertices = int(arquivo.readline().strip())
            for linha in arquivo:
                u, v = map(int, linha.split())
                self.adicionar_aresta(u, v)

    def escrever_informacoes(self, arquivo_saida):
        num_vertices, num_arestas, grau_minimo, grau_maximo, grau_medio, mediana = self.calcular_informacoes()

        with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
            arquivo.write(f"Número de vértices: {num_vertices}\n")
            arquivo.write(f"Número de arestas: {num_arestas}\n")
            arquivo.write(f"Grau mínimo: {grau_minimo}\n")
            arquivo.write(f"Grau máximo: {grau_maximo}\n")
            arquivo.write(f"Grau médio: {grau_medio:.2f}\n")
            arquivo.write(f"Mediana de grau: {mediana}\n")


if __name__ == "__main__":
    meu_grafo = Grafo()
    meu_grafo.ler_grafo("entrada.txt")
    meu_grafo.componentes_conexas() 
    meu_grafo.escrever_informacoes("informacoes.txt")



          
         
            


