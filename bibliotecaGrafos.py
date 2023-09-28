import gc as gc
import numpy as np
from bibliotecaFilaPilha import *
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

        return vetor #retorna o vetor de adjacência.
                    # ATENCAO, MELHORAR ESSE CODIGO, 2 FORS NAO EH LEGAL!
    
        
    def BFS(self, vertice_inicial): #BFS usando o vetor de adjacencia para representação (custo de O(m+n))
        vetor_marcacao = np.zeros(self.num_vertices, dtype= int) #inicializa a lista de marcação com zeros (desmarca todos os vértices).
        vetor_pais_e_niveis = np.full((self.num_vertices,),np.array([None, None])) #inicializa o vetor de pais e níveis com None. O formato do vetor apresenta vetores internos com [pai, nível] de cada vértice.
        vetor_pais_e_niveis[vertice_inicial -1][1] = 0 #Define o nível da raiz como 0. 
        Q = Fila() #Define a fila de explorados vazia
        vetor_marcacao[vertice_inicial -1] = 1 #Marca o vértice inicial #Marca o vértice inicial
        Q.enqueue(vertice_inicial) #Adiciona o vértice inicial na fila. #Adiciona o vértice inicial na raiz
        vetor_adjacencia = self.vetor_de_adjacencia()
        
        while Q.isEmpty() != True:
            v = Q.dequeue() #Remove o primeiro elemento da fila e atribui a v.
            for w in vetor_adjacencia[v-1]: #Para cada vizinho w de v
                if vetor_marcacao[w-1] == 0: #Se w não estiver marcado
                    vetor_marcacao[w-1] = 1 #Marca w
                    Q.enqueue(w) #Adiciona w na fila.
                    vetor_pais_e_niveis[w-1][0] = v #Define o pai de w como v.
                    vetor_pais_e_niveis[w-1][1] = vetor_pais_e_niveis[v-1][1] + 1 #Define o nível de w como o nível de v + 1.
                    
        return vetor_pais_e_niveis #retorna o vetor de pais e níveis.
    
    def DFS(self, vertice_inicial): #DFS usando o vetor de adjacencia para representação. Retorna a lista de pais e níveis no formato [pai, nível].
        vetor_marcacao = np.zeros(self.num_vertices, dtype= int) #inicializa a lista de marcação com zeros (desmarca todos os vértices).
        vetor_pais_e_niveis = np.full((self.num_vertices,),np.array([None, None])) #inicializa o vetor de pais e níveis com None. O formato do vetor apresenta vetores internos com [pai, nível] de cada vértice.
        vetor_pais_e_niveis[vertice_inicial -1][1] = 0 #Define o nível da raiz como 0.
        P = Pilha() #Define a pilha de explorados
        P.push(vertice_inicial) #Adiciona o vértice inicial na pilha.
        vetor_adjacencia = self.vetor_de_adjacencia()
        
        while P.isEmpty() != True: #Se a pilha não estiver vazia
            u = P.pop() #Remove o topo da pilha e atribui a u.
            if vetor_marcacao[u-1] == 0: #Se u não estiver marcado
                vetor_marcacao[u-1] = 1 #Marca u
                for v in vetor_adjacencia[u-1]: #Para cada vizinho v de u
                    P.push(v) #Adiciona v na pilha.
                    vetor_pais_e_niveis[v-1][0] = u #Define o pai de v como u.
                    vetor_pais_e_niveis[v-1][1] = vetor_pais_e_niveis[u-1][1] + 1 #Define o nível de v como o nível de u + 1.
        
        return vetor_pais_e_niveis #retorna o vetor de pais e níveis.
    
            


    def distancia(self, vertice_inicial, vertice_final): #Método para descobrir a distância entre dois vértices a partir da BFS (usa o vetor de adjacencia como reprentatividade)
        # Custo O(m+n) (custo da BFS)
        vetor_pais_e_niveis = self.BFS(vertice_inicial) #Inicializa o vetor de pais e niveis
        distancia = vetor_pais_e_niveis[vertice_final-1][1] #defie a distancia como o nível de explorados da BFS
        return distancia
        
        
    def diametro(self): #FAZER DEPOIS (Método que calcula o maior caminho mínimo entre 2 vértices quaisquer do grafos)
        #Custo = Custo(BFS) + O(grau(1) -1)
        # Jeito de otimizar: ter certeza que a iteração comece do vértice de menor grau
        diametro = 0
        for vertice in self.vertices:
            distancia = self.distancia(1, vertice) #Checa a distancia de todos os caminhos incluindo o vértice 1
            if distancia > diametro: 
                diametro = distancia
        return diametro        
            


