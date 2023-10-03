import numpy as np
from collections import deque
from scipy.sparse import lil_matrix

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = set()
        self.num_vertices = 0
        self.matriz_adjacencia = None
        self.vetor_adjacencia = None

    def calcular_estruturas_adjacencia(self):
        self.matriz_adjacencia = lil_matrix((self.num_vertices, self.num_vertices), dtype=int)
        self.vetor_adjacencia = [set() for _ in range(self.num_vertices)]

        for u, v in self.arestas:
            self.matriz_adjacencia[u - 1, v - 1] = 1
            self.matriz_adjacencia[v - 1, u - 1] = 1
            self.vetor_adjacencia[u - 1].add(v)
            self.vetor_adjacencia[v - 1].add(u)

    def adicionar_aresta(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.arestas.add((u, v))
        self.arestas.add((v, u))

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

    def matriz_de_adjacencia(self):
        return self.matriz_adjacencia

    def vetor_de_adjacencia(self):
        return self.vetor_adjacencia

    def imprimir_informacoes(self):
        num_vertices, num_arestas, grau_minimo, grau_maximo, grau_medio, mediana = self.calcular_informacoes()
        print("\nInformações do Grafo:")
        print(f"Número de vértices: {num_vertices}")
        print(f"Número de arestas: {num_arestas}")
        print(f"Grau mínimo: {grau_minimo}")
        print(f"Grau máximo: {grau_maximo}")
        print(f"Grau médio: {grau_medio:.2f}")
        print(f"Mediana de grau: {mediana}")

    def BFS(self, vertice_inicial, modo):
        fila = deque()
        fila.append(vertice_inicial)
        visitados = set([vertice_inicial])
        nivel = {vertice_inicial: 0}
        pais = {vertice_inicial: None}

        if modo == 1:
            matriz_adjacencia = self.matriz_adjacencia.toarray()
            while fila:
                u = fila.popleft()
                for v in range(self.num_vertices):
                    if matriz_adjacencia[u - 1][v] == 1 and v + 1 not in visitados:
                        visitados.add(v + 1)
                        fila.append(v + 1)
                        nivel[v + 1] = nivel[u] + 1
                        pais[v + 1] = u
        elif modo == 2:
            vetor_adjacencia = self.vetor_adjacencia
            while fila:
                u = fila.popleft()
                for v in vetor_adjacencia[u - 1]:
                    if v not in visitados:
                        visitados.add(v)
                        fila.append(v)
                        nivel[v] = nivel[u] + 1
                        pais[v] = u

        return pais, nivel

    def DFS(self, vertice_inicial, modo, visitados=None):
        if visitados is None:
            visitados = set()

        pais = {}
        nivel = {}
        pilha = deque()

        pilha.append(vertice_inicial)
        visitados.add(vertice_inicial)
        nivel[vertice_inicial] = 0

        if modo == 1:
            matriz_adjacencia = self.matriz_adjacencia.toarray()
            while pilha:
                u = pilha.pop()
                for v in range(self.num_vertices):
                    if matriz_adjacencia[u - 1][v] == 1 and v + 1 not in visitados:
                        visitados.add(v + 1)
                        pilha.append(v + 1)
                        nivel[v + 1] = nivel[u] + 1
                        pais[v + 1] = u
        elif modo == 2:
            vetor_adjacencia = self.vetor_adjacencia
            while pilha:
                u = pilha.pop()
                for v in vetor_adjacencia[u - 1]:
                    if v not in visitados:
                        visitados.add(v)
                        pilha.append(v)
                        nivel[v] = nivel[u] + 1
                        pais[v] = u

        resultado = (pais, nivel)
        return resultado

    def salvar_arvore_busca(self, pais, nivel, arquivo_saida):
        with open(arquivo_saida, 'w') as arquivo:
            for vertice, pai in pais.items():
                nivel_vertice = nivel[vertice]
                arquivo.write(f"Vértice {vertice}: Pai = {pai if pai is not None else 'N/A'}, Nível = {nivel_vertice}\n")

    def distancia(self, vertice_inicial, vertice_final, modo):
        fila = deque()
        fila.append(vertice_inicial)
        visitados = {vertice_inicial}
        nivel = {vertice_inicial: 0}

        if modo == 1:
            matriz_adjacencia = self.matriz_adjacencia
            while fila:
                u = fila.popleft()
                for v in range(self.num_vertices):
                    if matriz_adjacencia[u - 1][v] == 1 and v + 1 not in visitados:
                        visitados.add(v + 1)
                        fila.append(v + 1)
                        nivel[v + 1] = nivel[u] + 1
                        if v + 1 == vertice_final:
                            return nivel[vertice_final]
        elif modo == 2:
            vetor_adjacencia = self.vetor_adjacencia
            while fila:
                u = fila.popleft()
                for v in vetor_adjacencia[u - 1]:
                    if v not in visitados:
                        visitados.add(v)
                        fila.append(v)
                        nivel[v] = nivel[u] + 1
                        if v == vertice_final:
                            return nivel[vertice_final]

    def diametro(self):
        diametro = 0
        for vertice in self.vertices:
            distancia = self.distancia(1, vertice, 2)
            if distancia > diametro:
                diametro = distancia
        return diametro

    def componentes_conexas(self):
        componentes_conexas = []
        vetor_marcacao = np.zeros(self.num_vertices)
        for v in range(1, self.num_vertices + 1):
            if vetor_marcacao[v - 1] == 0:
                visitados = self.BFS(v, 2)[0]
                componentes_conexas.append(list(visitados.keys()))
                for vertice in visitados:
                    vetor_marcacao[vertice - 1] = 1

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

def verificar_entrada(vertice_inicial, num_vertices):
    if vertice_inicial < 1 or vertice_inicial > num_vertices:
        print(f"Vértice inicial inválido! Tente novamente. O intervalo do grafo é de 1 até {num_vertices}")
        return False
    return True

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Ler informações do Grafo")
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
        if escolha_representacao == 1 or escolha_representacao == 2:
            return escolha_representacao
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    meu_grafo = Grafo()
    meu_grafo.ler_grafo("grafo1.txt")
    meu_grafo.calcular_estruturas_adjacencia()
    meu_grafo.escrever_informacoes("informacoes.txt")

    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")
        print("\n")
        if opcao == '1':
            meu_grafo.imprimir_informacoes()
        elif opcao == '2':
            escolha_representacao = escolher_representacao()
            vertice_inicial = int(input("Digite o vértice inicial para a BFS: "))
            if verificar_entrada(vertice_inicial, meu_grafo.num_vertices):
                resultado = meu_grafo.BFS(vertice_inicial, escolha_representacao)
                print("Árvore de Busca em Largura (BFS):")
                for v in range(1, meu_grafo.num_vertices + 1):
                    if v in resultado[0]:
                        pai, nivel = resultado[0][v], resultado[1][v]
                        print(f"Vértice {v}: Pai = {pai if pai is not None else 'N/A'}, Nível = {nivel}")
                    else:
                        print(f"Vértice {v} não foi alcançado pela BFS.")
        elif opcao == '3':
            escolha_representacao = escolher_representacao()
            vertice_inicial = int(input("Digite o vértice inicial para a DFS: "))
            if verificar_entrada(vertice_inicial, meu_grafo.num_vertices):
                resultado = meu_grafo.DFS(vertice_inicial, escolha_representacao)
                print("Árvore de Busca em Profundidade (DFS):")
                for v in range(1, meu_grafo.num_vertices + 1):
                    if v in resultado[0]:
                        pai, nivel = resultado[0][v], resultado[1][v]
                        print(f"Vértice {v}: Pai = {pai if pai is not None else 'N/A'}, Nível = {nivel}")
                    else:
                        print(f"Vértice {v} não foi alcançado pela DFS.")
        elif opcao == '4':
            escolha_representacao = escolher_representacao()
            vertice_inicial = int(input("Digite o vértice inicial: "))
            vertice_final = int(input("Digite o vértice final: "))
            if verificar_entrada(vertice_inicial, meu_grafo.num_vertices) and verificar_entrada(vertice_final, meu_grafo.num_vertices):
                distancia = meu_grafo.distancia(vertice_inicial, vertice_final, escolha_representacao)
                print(f"\nA distância entre {vertice_inicial} e {vertice_final} é {distancia}.")
        elif opcao == '5':
            diametro = meu_grafo.diametro()
            print(f"O diâmetro aproximado do grafo é {diametro}.")
        elif opcao == '6':
            resultado = meu_grafo.componentes_conexas()
            print("Componentes conexas do grafo:", resultado)
        elif opcao == '7':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
