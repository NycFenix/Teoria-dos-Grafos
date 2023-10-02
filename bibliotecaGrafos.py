import gc as gc
import numpy as np
from bibliotecaFilaPilha import *

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = []
        self.num_vertices = 0
        self.CCs = set()

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
        matriz = np.zeros((self.num_vertices,self.num_vertices), int) #inicializa a matriz com zeros.
        for aresta in self.arestas:  #percorre a lista de arestas.
            x, y = aresta #atribui os valores de aresta a x e y.
            matriz[x-1][y-1] = 1
            matriz[y-1][x-1] = 1   #Assumindo que o grafo não é direcionado, atribui as ligações à matriz.
            
        return matriz #retorna a matriz de adjacência.
    
    def vetor_de_adjacencia(self): #Método para representação em Lista de adjacência.
        vetor = np.zeros((self.num_vertices, ), Fila)
        for n in range(self.num_vertices):
            vetor[n] = Fila() #Adiciona uma fila vazia para cada vértice.
        for aresta in self.arestas:
            g, h = aresta
            vetor[g-1].uniao(h)
            vetor[h-1].uniao(g)
                    
        return vetor
    
    def imprimir_informacoes(self):
        meu_grafo.escrever_informacoes("informacoes.txt")
        num_vertices, num_arestas, grau_minimo, grau_maximo, grau_medio, mediana = self.calcular_informacoes()
        print("\nInformações do Grafo:")
        print(f"Número de vértices: {num_vertices}")
        print(f"Número de arestas: {num_arestas}")
        print(f"Grau mínimo: {grau_minimo}")
        print(f"Grau máximo: {grau_maximo}")
        print(f"Grau médio: {grau_medio:.2f}")
        print(f"Mediana de grau: {mediana}")            
                
        
    def BFS(self, vertice_inicial, modo): 
        self.CCs = set()
        if modo == 1: # BFS usando matriz de adjacência para representação
            matriz_adjacencia = self.matriz_de_adjacencia()
            vetor_marcacao = np.zeros(self.num_vertices, dtype=int)  # Inicializa a lista de marcação com zeros (desmarca todos os vértices).
            vetor_pais_e_niveis = np.full((self.num_vertices, 2), np.array([None, None]))  # Inicializa o vetor de pais e níveis com None. O formato do vetor apresenta vetores internos com [pai, nível] de cada vértice.
            vetor_pais_e_niveis[vertice_inicial - 1][1] = 0  # Define o nível da raiz como 0.
            Q = Fila()  # Define a fila de explorados vazia
            vetor_marcacao[vertice_inicial - 1] = 1  # Marca o vértice inicial
            Q.enqueue(vertice_inicial)  # Adiciona o vértice inicial na fila.
            self.CCs.add(vertice_inicial)
            while not Q.isEmpty():
                v = Q.dequeue()  # Remove o primeiro elemento da fila e atribui a v.
                for w in range(self.num_vertices):
                    if matriz_adjacencia[v - 1][w] == 1 and vetor_marcacao[w] == 0:
                        vetor_marcacao[w] = 1  # Marca w
                        self.CCs.add(w)
                        Q.enqueue(w + 1)  # Adiciona w na fila.
                        vetor_pais_e_niveis[w][0] = v  # Define o pai de w como v.
                        vetor_pais_e_niveis[w][1] = vetor_pais_e_niveis[v - 1][1] + 1  # Define o nível de w como o nível de v + 1.

            with open("BFS_matriz_adjacencia", 'w', encoding='utf-8') as arquivo:
                        arquivo.write("Árvore de Busca em Largura (BFS):\n")
                        for v in range(self.num_vertices):
                            if vetor_pais_e_niveis[v][0] is not None:
                                arquivo.write(f"Vértice {v+1}: Pai = {vetor_pais_e_niveis[v][0]}, Nível = {vetor_pais_e_niveis[v][1]}\n")
            return vetor_pais_e_niveis  # Retorna o vetor de pais e níveis.                        
            
            return vetor_pais_e_niveis  # Retorna o vetor de pais e níveis.
        
        if modo == 2: #BFS usando o vetor de adjacencia para representação (custo de O(m+n))
            vetor_marcacao = np.zeros(self.num_vertices, dtype= int) #inicializa a lista de marcação com zeros (desmarca todos os vértices).
        
            vetor_pais_e_niveis = np.full((self.num_vertices,2),np.array([None, None])) #inicializa o vetor de pais e níveis com None. O formato do vetor apresenta vetores internos com [pai, nível] de cada vértice.
            
            vetor_pais_e_niveis[vertice_inicial -1][1] = 0 #Define o nível da raiz como 0. 
            Q = Fila() #Define a fila de explorados vazia
            vetor_marcacao[vertice_inicial -1] = 1 #Marca o vértice inicial #Marca o vértice inicial
            Q.enqueue(vertice_inicial) #Adiciona o vértice inicial na fila. #Adiciona o vértice inicial na raiz
            self.CCs.add(vertice_inicial)
            vetor_adjacencia = self.vetor_de_adjacencia()
            
            while Q.isEmpty() != True:
                v = Q.dequeue() #Remove o primeiro elemento da fila e atribui a v.
                vizinho_atual = vetor_adjacencia[v-1].head #Atribui o primeiro vizinho de v a vizinho_atual.
                while vizinho_atual: #Percorre os vizinhos de v
                    valor_vizinho = vizinho_atual.valor #Atribui o valor numérico do vizinho atual a valor_vizinho
                    if vetor_marcacao[valor_vizinho-1] == 0: #Se nodo atual nao estiver marcado...
                        vetor_marcacao[valor_vizinho-1] = 1 #... marca nodo atual
                        self.CCs.add(valor_vizinho)
                        Q.enqueue(valor_vizinho) #Adiciona vizinho atual na fila
                        vetor_pais_e_niveis[valor_vizinho-1][0] = v #Define o pai de nodo atual como v.
                        vetor_pais_e_niveis[valor_vizinho-1][1] = vetor_pais_e_niveis[v-1][1] + 1 #Define o nível de nodo atual como o nível de v + 1.
                    vizinho_atual = vizinho_atual.next #Passa para o próximo vizinho de v.   
                      
                with open("BFS_vetor_adjacencia", 'w', encoding='utf-8') as arquivo:
                                        arquivo.write("Árvore de Busca em Largura (BFS) usando Vetor de Adjacência:\n")
                                        for v in range(self.num_vertices):
                                            if vetor_pais_e_niveis[v][0] is not None:
                                                arquivo.write(f"Vértice {v+1}: Pai = {vetor_pais_e_niveis[v][0]}, Nível = {vetor_pais_e_niveis[v][1]}\n")    
                        
            return vetor_pais_e_niveis #retorna o vetor de pais e níveis.
    
    def DFS(self, vertice_inicial, modo): 
        self.CCs = set()
        if modo == 2: #DFS usando o vetor de adjacencia para representação. Retorna a lista de pais e níveis no formato [pai, nível].
            vetor_marcacao = np.zeros(self.num_vertices, dtype= int)
            vetor_adjacencia = self.vetor_de_adjacencia() #Inicializa vetor de adjacencia
            
            vetor_pais_e_niveis = np.full((self.num_vertices,2),np.array([None, None])) #inicializa o vetor de pais e níveis com None. O formato do vetor apresenta vetores internos com [pai, nível] de cada vértice.
            vetor_pais_e_niveis[vertice_inicial -1][1] = 0 #Define o nível da raiz como 0. 
            vetor_marcacao[vertice_inicial -1] = 1 
            
            P = Pilha() #Define a pilha de explorados vazia
            P.push(vertice_inicial) #Adiciona o vértice inicial na pilha.
            self.CCs.add(vertice_inicial)
            while P.isEmpty() != True: #Enquanto a pilha não estiver vazia...
                u = P.pop() #Remove o primeiro elemento da pilha e atribui a u.
                vizinho_atual = vetor_adjacencia[u-1].head
            
                while vizinho_atual: #Percorre os vizinhos de u
                    valor_vizinho = vizinho_atual.valor
                    if vetor_marcacao[valor_vizinho-1] == 0: #Se u não estiver marcado...
                        vetor_marcacao[valor_vizinho-1] = 1 #... marca u
                        
                        P.push(valor_vizinho)
                        vetor_pais_e_niveis[valor_vizinho-1][0] = u #Define o pai de nodo atual como u.
                        vetor_pais_e_niveis[valor_vizinho-1][1] = vetor_pais_e_niveis[u-1][1] + 1 #Define o nível de nodo atual como o nível de u + 1.

                    vizinho_atual = vizinho_atual.next #Avanca para o proximo vizinho de u
                        
            return vetor_pais_e_niveis
                
                
                
                #Versao antiga usando vetores numpy              
               
                # for v in vetor_adjacencia[u-1]: #Para cada vizinho v de u
                #     P.push(v) #Adiciona v na pilha.
                #     vetor_pais_e_niveis[v-1][0] = u #Define o pai de v como u.
                #     vetor_pais_e_niveis[v-1][1] = vetor_pais_e_niveis[u-1][1] + 1 #Define o nível de v como o nível de u + 1.
        
       

    def distancia(self, vertice_inicial, vertice_final, modo): #Método para descobrir a distância entre dois vértices a partir da BFS (usa o vetor de adjacencia como reprentatividade)
        # Custo O(m+n) (custo da BFS)
        vetor_pais_e_niveis = self.BFS(vertice_inicial, modo) #Inicializa o vetor de pais e niveis
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
    
    def componentes_conexas(self):
        componentes_conexas = np.array([])
        self.vetor_marcacao = np.zeros(self.num_vertices)
        for v in range(1, self.num_vertices):
            if self.vetor_marcacao[v-1] == 0: #Se não estiver marcado
                self.BFS(v)
                componentes_conexas = np.concatenate((componentes_conexas, np.array([self.CCs])), axis = 0)
                
        return componentes_conexas
            
            
    def ler_grafo(self, arquivo_entrada):
        with open(arquivo_entrada, 'r') as arquivo:
            self.num_vertices = int(arquivo.readline().strip())
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

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Ler informacoes do Grafo")
    print("2. Percorrer o grafo utilizando Busca em Largura (BFS)")
    print("3. Percorrer o grafo utilizando Busca em Profundidade (DFS)")
    print("4. Determinar distância entre dois vértices do grafo")
    print("5. Calcular Diâmetro do Grafo")
    print("6. Descobrir Componentes Conexas do grafo")
    print("7. Sair")   


if __name__ == "__main__":
    meu_grafo = Grafo()
    meu_grafo.ler_grafo("entrada.txt")
    meu_grafo.escrever_informacoes("informacoes.txt")
    print("Escolha a representação do grafo:")
    print("1. Matriz de Adjacência")
    print("2. Vetor de Adjacência")
    escolha_representacao = int(input("Digite o número da opção desejada: "))
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            meu_grafo.imprimir_informacoes()
        elif opcao == '2':
            vertice_inicial = int(input("Digite o vértice inicial para a BFS: "))
            print(meu_grafo.BFS(vertice_inicial,escolha_representacao))
        elif opcao == '3':
            vertice_inicial = int(input("Digite o vértice inicial para a DFS: "))
            print(meu_grafo.DFS(vertice_inicial,escolha_representacao))
        elif opcao == '4':
            vertice_inicial = int(input("Digite o vértice inicial: "))
            vertice_final = int(input("Digite o vértice final: "))
            meu_grafo.distancia(vertice_inicial, vertice_final, escolha_representacao)
        elif opcao == '5':
            meu_grafo.diametro()
        elif opcao == '6':
            meu_grafo.componentes_conexas()
        elif opcao == '7':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


