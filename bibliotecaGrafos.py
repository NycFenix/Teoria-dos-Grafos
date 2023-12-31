import gc as gc
import psutil
import numpy as np
np.set_printoptions(threshold=np.inf)
from bibliotecaFilaPilha import *
import time
import sys
from funcoesAuxiliares import destroy
class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = np.empty((0, 2), int)
        self.num_vertices = 0
        self.CCs = set()
        self.vetor_marcacao = np.array([])

    def adicionar_aresta(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.arestas = np.concatenate((self.arestas, np.array([[u, v]])))

    def calcular_informacoes(self):
        self.num_vertices = len(self.vertices)
        num_arestas = self.arestas.size
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

    

    def matriz_de_adjacencia(self): #Método para representação em Matriz de ajacência usando o método np.zeros.
        
        #tempo_inicial = time.time()
        matriz = np.zeros((self.num_vertices,self.num_vertices), int) #inicializa a matriz com zeros.
        for aresta in self.arestas:  #percorre a lista de arestas.
                #x, y = aresta #atribui os valores de aresta a x e y.
            x = aresta[0]
            y = aresta[1]
            matriz[x-1][y-1] = 1
            matriz[y-1][x-1] = 1
            destroy(x)
            destroy(y)
            
            
            #Assumindo que o grafo não é direcionado, atribui as ligações à matriz.
        # t_final = time.time()
        # print (t_final - tempo_inicial)
        
        return matriz #retorna a matriz de adjacência.
    
    def vetor_de_adjacencia(self): #Método para representação em Lista de adjacência.
        vetor = np.zeros((self.num_vertices, ), Fila)
        for n in range(self.num_vertices):
            vetor[n] = Fila() #Adiciona uma fila vazia para cada vértice.
        for aresta in self.arestas:
            g, h = aresta
            vetor[g-1].uniao(h)
            vetor[h-1].uniao(g)

        destroy(vetor)
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
        gc.collect()
        
        
        self.CCs = set()

        if modo == 1:  # BFS usando matriz de adjacência para representação
            matriz_adjacencia = self.matriz_de_adjacencia()
            self.vetor_marcacao = np.zeros(self.num_vertices, dtype=int)
            vetor_pais_e_niveis = np.full((self.num_vertices, 2), np.array([None, None]))
            vetor_pais_e_niveis[vertice_inicial - 1][1] = 0
            Q = Fila()
            self.vetor_marcacao[vertice_inicial - 1] = 1
            Q.enqueue(vertice_inicial)
            self.CCs.add(vertice_inicial)
            while not Q.isEmpty():
                v = Q.dequeue()
                for w in range(self.num_vertices):
                    if matriz_adjacencia[v - 1][w] == 1 and self.vetor_marcacao[w] == 0:
                        self.vetor_marcacao[w] = 1
                        self.CCs.add(w)
                        Q.enqueue(w + 1)
                        vetor_pais_e_niveis[w][0] = v
                        vetor_pais_e_niveis[w][1] = vetor_pais_e_niveis[v - 1][1] + 1

            with open("BFS_matriz_adjacencia.txt", 'w', encoding='utf-8') as arquivo:
                arquivo.write("Árvore de Busca em Largura (BFS):\n")
                for v in range(self.num_vertices):
                    if vetor_pais_e_niveis[v][0] is not None:
                        arquivo.write(f"Vértice {v+1}: Pai = {vetor_pais_e_niveis[v][0]}, Nível = {vetor_pais_e_niveis[v][1]}\n")

            return vetor_pais_e_niveis

        if modo == 2:  # BFS usando o vetor de adjacência para representação
            self.vetor_marcacao = [0] * self.num_vertices  # Inicialize como uma lista
            vetor_pais_e_niveis = np.full((self.num_vertices, 2), np.array([None, None]))
            vetor_pais_e_niveis[vertice_inicial - 1][1] = 0
            Q = Fila()
            self.vetor_marcacao[vertice_inicial - 1] = 1
            Q.enqueue(vertice_inicial)
            self.CCs.add(vertice_inicial)
            vetor_adjacencia = self.vetor_de_adjacencia()

            while not Q.isEmpty():
                v = Q.dequeue()
                vizinho_atual = vetor_adjacencia[v - 1].head
                while vizinho_atual:
                    valor_vizinho = vizinho_atual.valor
                    if self.vetor_marcacao[valor_vizinho - 1] == 0:
                        self.vetor_marcacao[valor_vizinho - 1] = 1
                        self.CCs.add(valor_vizinho)
                        Q.enqueue(valor_vizinho)
                        vetor_pais_e_niveis[valor_vizinho - 1][0] = v
                        vetor_pais_e_niveis[valor_vizinho - 1][1] = vetor_pais_e_niveis[v - 1][1] + 1
                    vizinho_atual = vizinho_atual.next


            with open("BFS_vetor_adjacencia.txt", 'w', encoding='utf-8') as arquivo:
                arquivo.write("Árvore de Busca em Largura (BFS) usando Vetor de Adjacência:\n")
                for v in range(self.num_vertices):
                    if vetor_pais_e_niveis[v][0] is not None:
                        arquivo.write(f"Vértice {v+1}: Pai = {vetor_pais_e_niveis[v][0]}, Nível = {vetor_pais_e_niveis[v][1]}\n")

            return vetor_pais_e_niveis
                       
        
        if modo == 2: #BFS usando o vetor de adjacencia para representação (custo de O(m+n))
            self.vetor_marcacao = np.zeros(self.num_vertices, dtype= int) #inicializa a lista de marcação com zeros (desmarca todos os vértices).
        
            vetor_pais_e_niveis = np.full((self.num_vertices,2),np.array([None, None])) #inicializa o vetor de pais e níveis com None. O formato do vetor apresenta vetores internos com [pai, nível] de cada vértice.
            
            vetor_pais_e_niveis[vertice_inicial -1][1] = 0 #Define o nível da raiz como 0. 
            Q = Fila() #Define a fila de explorados vazia
            self.vetor_marcacao[vertice_inicial -1] = 1 #Marca o vértice inicial #Marca o vértice inicial
            Q.enqueue(vertice_inicial) #Adiciona o vértice inicial na fila. #Adiciona o vértice inicial na raiz
            self.CCs.add(vertice_inicial)
            vetor_adjacencia = self.vetor_de_adjacencia()
            
            while Q.isEmpty() != True:
                v = Q.dequeue() #Remove o primeiro elemento da fila e atribui a v.
                vizinho_atual = vetor_adjacencia[v-1].head #Atribui o primeiro vizinho de v a vizinho_atual.
                while vizinho_atual: #Percorre os vizinhos de v
                    valor_vizinho = vizinho_atual.valor #Atribui o valor numérico do vizinho atual a valor_vizinho
                    if self.vetor_marcacao[valor_vizinho-1] == 0: #Se nodo atual nao estiver marcado...
                        self.vetor_marcacao[valor_vizinho-1] = 1 #... marca nodo atual
                        self.CCs.add(valor_vizinho)
                        Q.enqueue(valor_vizinho) #Adiciona vizinho atual na fila
                        vetor_pais_e_niveis[valor_vizinho-1][0] = v #Define o pai de nodo atual como v.
                        vetor_pais_e_niveis[valor_vizinho-1][1] = vetor_pais_e_niveis[v-1][1] + 1 #Define o nível de nodo atual como o nível de v + 1.
                    vizinho_atual = vizinho_atual.next #Passa para o próximo vizinho de v.   

                with open("BFS_vetor_adjacencia.txt", 'w', encoding='utf-8') as arquivo:
                                        arquivo.write("Árvore de Busca em Largura (BFS) usando Vetor de Adjacência:\n")
                                        for v in range(self.num_vertices):
                                            if vetor_pais_e_niveis[v][0] is not None:
                                                arquivo.write(f"Vértice {v+1}: Pai = {vetor_pais_e_niveis[v][0]}, Nível = {vetor_pais_e_niveis[v][1]}\n")    
                        
            return vetor_pais_e_niveis #retorna o vetor de pais e níveis.
    
    def DFS(self, vertice_inicial, modo):
        gc.collect()
        self.CCs = []  # Use uma lista em vez de um conjunto
        self.vetor_marcacao = np.zeros(self.num_vertices, dtype=int)

        if modo == 1:  # DFS usando matriz de adjacência para representação
            matriz_adjacencia = self.matriz_de_adjacencia()
            vetor_pais_e_niveis = [[None, None] for _ in range(self.num_vertices)]  # Use uma lista
            vetor_pais_e_niveis[vertice_inicial - 1][1] = 0
            P = Pilha()
            self.vetor_marcacao[vertice_inicial - 1] = 1
            P.push(vertice_inicial)
            self.CCs.append(vertice_inicial)  # Use append para adicionar à lista

            while not P.isEmpty():
                v = P.pop()
                for w in range(self.num_vertices):
                    if matriz_adjacencia[v - 1][w] == 1 and self.vetor_marcacao[w] == 0:
                        self.vetor_marcacao[w] = 1
                        P.push(w + 1)
                        vetor_pais_e_niveis[w][0] = v
                        vetor_pais_e_niveis[w][1] = vetor_pais_e_niveis[v - 1][1] + 1

            with open("DFS_matriz_adjacencia.txt", 'w', encoding='utf-8') as arquivo:
                arquivo.write("Árvore de Busca em Profundidade (DFS) usando Matriz de Adjacência:\n")
                for v in range(self.num_vertices):
                    if vetor_pais_e_niveis[v][0] is not None:
                        arquivo.write(f"Vértice {v + 1}: Pai = {vetor_pais_e_niveis[v][0]}, Nível = {vetor_pais_e_niveis[v][1]}\n")

            return vetor_pais_e_niveis

        if modo == 2:  # DFS usando o vetor de adjacência para representação
            vetor_adjacencia = self.vetor_de_adjacencia()
            vetor_pais_e_niveis = [[None, None] for _ in range(self.num_vertices)]
            vetor_pais_e_niveis[vertice_inicial - 1][1] = 0
            P = Pilha()
            self.vetor_marcacao[vertice_inicial - 1] = 1
            P.push(vertice_inicial)
            self.CCs.append(vertice_inicial)

            while not P.isEmpty():
                u = P.pop()
                vizinho_atual = vetor_adjacencia[u - 1].head

                while vizinho_atual:
                    valor_vizinho = vizinho_atual.valor
                    if self.vetor_marcacao[valor_vizinho - 1] == 0:
                        self.vetor_marcacao[valor_vizinho - 1] = 1
                        P.push(valor_vizinho)
                        vetor_pais_e_niveis[valor_vizinho - 1][0] = u
                        vetor_pais_e_niveis[valor_vizinho - 1][1] = vetor_pais_e_niveis[u - 1][1] + 1

                    vizinho_atual = vizinho_atual.next

            with open("DFS_vetor_adjacencia.txt", 'w', encoding='utf-8') as arquivo:
                arquivo.write("Árvore de Busca em Profundidade (DFS) usando Vetor de Adjacência:\n")
                for v in range(self.num_vertices):
                    if vetor_pais_e_niveis[v][0] is not None:
                        arquivo.write(f"Vértice {v + 1}: Pai = {vetor_pais_e_niveis[v][0]}, Nível = {vetor_pais_e_niveis[v][1]}\n")

            return vetor_pais_e_niveis

                
                


    def distancia(self, vertice_inicial, vertice_final, modo): #Método para descobrir a distância entre dois vértices a partir da BFS (usa o vetor de adjacencia como reprentatividade)
        # Custo O(m+n) (custo da BFS)
        vetor_pais_e_niveis = self.BFS(vertice_inicial, modo) #Inicializa o vetor de pais e niveis
        distancia = vetor_pais_e_niveis[vertice_final-1][1] #define a distancia como o nível de explorados da BFS
        del(vetor_pais_e_niveis)
        
        return distancia
        
        
    def diametro(self): #FAZER DEPOIS (Método que calcula o maior caminho mínimo entre 2 vértices quaisquer do grafos)
        #Custo = Custo(BFS) + O(grau(1) -1)
        # Jeito de otimizar: ter certeza que a iteração comece do vértice de menor grau
        diametro = 0
        for vertice in self.vertices:
            distancia = self.distancia(1, vertice, 2) #Checa a distancia de todos os caminhos incluindo o vértice 1 (usando vetor de adjacencia)
            if distancia > diametro: 
                diametro = distancia
        return diametro        

    def componentes_conexas(self):
        gc.collect()
        componentes_conexas = np.array([])
        self.vetor_marcacao = np.zeros(self.num_vertices)
        for v in range(1, self.num_vertices):
            if self.vetor_marcacao[v-1] == 0: #Se não estiver marcado
                self.BFS(v, 2)
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
        
        del(num_vertices, num_arestas, grau_minimo, grau_maximo, grau_medio, mediana)

def verificar_entrada(vertice_inicial): # Verifica se o vértice inicial é válido
    if vertice_inicial < 1 or vertice_inicial > meu_grafo.num_vertices:
        print("Vértice inicial inválido! Tente novamente. O invervalo do grafo é de 1 até",meu_grafo.num_vertices)
        return False
    return True

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Ler informacoes do Grafo")
    print("2. Percorrer o grafo utilizando Busca em Largura (BFS)")
    print("3. Percorrer o grafo utilizando Busca em Profundidade (DFS)")
    print("4. Determinar distância entre dois vértices do grafo")
    print("5. Calcular Diâmetro do Grafo")
    print("6. Descobrir Componentes Conexas do grafo")
    print("7. Sair")   

def escolher_representacao():
    while True:
        print("Escolha a representação do grafo:")
        print("1. Matriz de Adjacência")
        print("2. Vetor de Adjacência")
        escolha_representacao = int(input("Digite o número da opção desejada: "))
        if escolha_representacao==1 or escolha_representacao==2:
            return escolha_representacao 
        else:
            print("Opção inválida! Tente novamente.\n")


if __name__ == "__main__":
    meu_grafo = Grafo()
    meu_grafo.ler_grafo("grafo1.txt")
    meu_grafo.escrever_informacoes("informacoes.txt")
    print("Tamanho em bytes do grafo:", sys.getsizeof(meu_grafo)) #o objeto grafo ocupa 48 bytes 
          
    
    
    print("Escolha a representação do grafo:")
    print("1. Matriz de Adjacência")
    print("2. Vetor de Adjacência")
    escolha_representacao = int(input("Digite o número da opção desejada: "))
    
    # print(representacao)
    print('% de memória RAM usada:', psutil.virtual_memory()[2])   
    print("Memória em GB: ", psutil.virtual_memory()[3] / 1000000000)
    
    # del(representacao)
    
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")
        print("\n")
        if opcao == '1':
            meu_grafo.imprimir_informacoes()
        elif opcao == '2':
            escolha_representacao = escolher_representacao()
            vertice_inicial = int(input("Digite o vértice inicial para a BFS: "))
            if verificar_entrada(vertice_inicial):
                resultado = meu_grafo.BFS(vertice_inicial, escolha_representacao)
                print("Árvore de Busca em Largura (BFS):")
                for v in range(meu_grafo.num_vertices):
                    if resultado[v][0] is not None:
                        pai, nivel = resultado[v]
                        print(f"Vértice {v+1}: Pai = {pai}, Nível = {nivel}")
                    else:
                        print(f"Vértice {v+1} não foi alcançado pela BFS.")
                        
        elif opcao == '3':
            escolha_representacao = escolher_representacao()
            vertice_inicial = int(input("Digite o vértice inicial para a DFS: "))
            if verificar_entrada(vertice_inicial):
                resultado  = meu_grafo.DFS(vertice_inicial,escolha_representacao)
                print("Árvore de Busca em Profundidade (DFS):")
                for v in range(meu_grafo.num_vertices):
                                if resultado[v][0] is not None:
                                    pai, nivel = resultado[v]
                                    print(f"Vértice {v+1}: Pai = {pai}, Nível = {nivel}")
                                else:
                                    print(f"Vértice {v+1} não foi alcançado pela DFS.")
            
            # del(resultado)
        elif opcao == '4':
            escolha_representacao = escolher_representacao()
            if verificar_entrada(vertice_inicial):
                vertice_inicial = int(input("Digite o vértice inicial: "))
                vertice_final = int(input("Digite o vértice final: "))
                distancia = meu_grafo.distancia(vertice_inicial, vertice_final, escolha_representacao)
                print(f"A distância entre {vertice_inicial} e {vertice_final} é {distancia}.")
                
                del(vertice_inicial, vertice_final, distancia)
        elif opcao == '5':
            diametro = meu_grafo.diametro()
            print(f"O diâmetro do grafo é {diametro}.")
            del(diametro)
        elif opcao == '6':
            resultado = meu_grafo.componentes_conexas()
            print("Componentes conexas do grafo:",resultado)
            # del(resultado)
        elif opcao == '7':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


