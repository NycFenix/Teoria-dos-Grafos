import gc as gc
import numpy as np

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = []
        self.num_vertices = 0
    def adicionar_aresta(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.arestas.append((u, v))

    def calcular_informacoes(self):
        self.num_vertices = len(self.vertices)
        num_arestas = len(self.arestas)
        graus = [0] * self.num_vertices

        for u, v in self.arestas:
            graus[u - 1] += 1
            graus[v - 1] += 1

        grau_minimo = min(graus)
        grau_maximo = max(graus)
        grau_medio = sum(graus) / self.num_vertices

        graus.sort()
        mediana = graus[self.num_vertices // 2]

        return self.num_vertices, num_arestas, grau_minimo, grau_maximo, grau_medio, mediana

    def componentes_conexas(self):
        # Implementar aqui o algoritmo BFS ou DFS para encontrar as componentes conexas.
        pass

    def matriz_de_adjacencia(self): #Método para representação em Matriz de ajacência usando o método np.zeros.
        matriz = np.zeros(self.num_vertices, self.num_vertices, dtype= int) #inicializa a matriz com zeros.
        for aresta in self.arestas:  #percorre a lista de arestas.
            x, y = aresta #atribui os valores de aresta a x e y.
            matriz[x][y] = 1
            matriz[y][x] = 1   #Assumindo que o grafo não é direcionado, atribui as ligações à matriz.
            
        return matriz #retorna a matriz de adjacência.
    
    def vetor_de_adjacencia(self): #Método para representação em Lista de adjacência.
        vetor = np.full(self.num_vertices, np.array([])) #Inicializa o vetor com arrays vazios.
        for vertice in self.vertices: #percorre a lista de arestas.
            for aresta in self.arestas: #percorre a lista de arestas.
                if vertice == self.arestas[vertice-1][0]:
                    vetor[vertice-1] = np.union1d(vetor[vertice-1], vertice) #Adiciona esse vértice na lista de vizinhos do vértice atual.

                    # ATENCAO, MELHORAR ESSE CODIGO, 2 FORS NAO EH LEGAL!
    
        
            

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



          
         
            


