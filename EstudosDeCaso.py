from bibliotecaGrafos import Grafo
import time

# Função para medir o uso de memória
def medir_memoria():
    import psutil
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # Retorna em MB

# Função para realizar um teste de busca em largura (BFS)
def teste_bfs(grafo, num_execucoes=100):
    print("Teste de Busca em Largura (BFS):")
    soma_tempo = 0

    for _ in range(num_execucoes):
        inicio = time.time()
        resultado_bfs = grafo.BFS(1, 1)  # Execute BFS a partir do vértice 1
        fim = time.time()
        tempo_execucao = fim - inicio
        soma_tempo += tempo_execucao

    tempo_medio = soma_tempo / num_execucoes
    print(f"Tempo médio de execução de BFS: {tempo_medio:.6f} segundos")

# Função para realizar um teste de busca em profundidade (DFS)
def teste_dfs(grafo, num_execucoes=100):
    print("Teste de Busca em Profundidade (DFS):")
    soma_tempo = 0

    for _ in range(num_execucoes):
        inicio = time.time()
        resultado_dfs = grafo.DFS(1, 1)  # Execute DFS a partir do vértice 1
        fim = time.time()
        tempo_execucao = fim - inicio
        soma_tempo += tempo_execucao

    tempo_medio = soma_tempo / num_execucoes
    print(f"Tempo médio de execução de DFS: {tempo_medio:.6f} segundos")

# Função para realizar o estudo de caso 1 (memória)
def estudio_de_caso_1(grafo):
    print("Estudo de Caso 1: Comparação de Memória")
    
    # Calcule a quantidade de memória antes de criar a matriz de adjacência
    memoria_antes = medir_memoria()
    
    # Calcule a estrutura de adjacência (matriz de adjacência)
    grafo.calcular_estruturas_adjacencia()
    
    # Calcule a quantidade de memória após a criação da matriz de adjacência
    memoria_depois = medir_memoria()
    
    # Calcule a diferença de memória em MB
    diferenca_memoria = memoria_depois - memoria_antes
    
    print(f"Memória antes da matriz de adjacência: {memoria_antes:.2f} MB")
    print(f"Memória após a matriz de adjacência: {memoria_depois:.2f} MB")
    print(f"Diferença de memória: {diferenca_memoria:.2f} MB")

# Função para realizar o estudo de caso 2 (BFS)
def estudio_de_caso_2(grafo):
    print("Estudo de Caso 2: Comparação de Tempo de Execução (BFS)")
    teste_bfs(grafo)

# Função para realizar o estudo de caso 3 (DFS)
def estudio_de_caso_3(grafo):
    print("Estudo de Caso 3: Comparação de Tempo de Execução (DFS)")
    teste_dfs(grafo)

# Função principal
def main():
    grafo = Grafo()
    grafo.ler_grafo("grafo_2.txt")
    
    # Estudo de Caso 1: Comparação de Memória
    estudio_de_caso_1(grafo)
    
    # Estudo de Caso 2: Comparação de Tempo de Execução (BFS)
    estudio_de_caso_2(grafo)
    
    # Estudo de Caso 3: Comparação de Tempo de Execução (DFS)
    estudio_de_caso_3(grafo)

if __name__ == "__main__":
    main()
