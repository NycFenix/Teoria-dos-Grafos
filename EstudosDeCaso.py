from bibliotecaGrafos import Grafo
import time

# Função para medir o uso de memória
def medir_memoria():
    import psutil
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # Retorna em MB


# Função principal para realizar o estudo de caso 1 da matriz de adjacência (alocação de memória)
def estudo_de_caso_matriz(grafo):
    print("--------Estudo de Caso 1 - Matriz de Adjacência--------")
    # Medir memória antes de criar a matriz de adjacência
    memoria_antes = medir_memoria()
    # Criar a matriz de adjacência
    grafo.calcular_matriz_adjacencia()
    # Medir memória após criar a matriz de adjacência
    memoria_depois = medir_memoria()
    # Calcular a diferença de memória em MB
    diferenca_memoria = memoria_depois - memoria_antes
    print(f"Memória antes da matriz de adjacência: {memoria_antes:.2f} MB")
    print(f"Memória após a matriz de adjacência: {memoria_depois:.2f} MB")
    print(f"Diferença de memória (Matriz): {diferenca_memoria:.2f} MB")

# Função principal para realizar o estudo de caso 1 do vetor de adjacência (alocação de memória)
def estudo_de_caso_vetor(grafo):
    print("--------Estudo de Caso 1 - Vetor de Adjacência--------")
    # Medir memória antes de criar a matriz de adjacência
    memoria_antes = medir_memoria()
    # Criar a matriz de adjacência
    grafo.calcular_vetor_adjacencia()
    # Medir memória após criar a matriz de adjacência
    memoria_depois = medir_memoria()
    # Calcular a diferença de memória em MB
    diferenca_memoria = memoria_depois - memoria_antes
    print(f"Memória antes da vetor de adjacência: {memoria_antes:.2f} MB")
    print(f"Memória após a vetor de adjacência: {memoria_depois:.2f} MB")
    print(f"Diferença de memória (Vetor): {diferenca_memoria:.2f} MB")
#====================================================================================================
#Estudo de caso 2 - tempo de execucao BFS

#BFS com matriz
def teste_bfs_matriz(grafo):
    print("\n--------Estudo de Caso 2: Comparação de Tempo de Execução (BFS com matriz)--------")
    inicio = time.time()
    resultado_bfs = grafo.BFS(1, 1)  # Execute BFS a partir do vértice 1
    fim = time.time()
    tempo_execucao = fim - inicio
    print(f"Tempo de execução de BFS: {tempo_execucao:.6f} segundos")

#BFS com vetor
def teste_bfs_vetor(grafo):
    print("\n--------Estudo de Caso 2: Comparação de Tempo de Execução (BFS com vetor)--------")
    inicio = time.time()
    resultado_bfs = grafo.BFS(1, 2)  # Execute BFS a partir do vértice 1
    fim = time.time()
    tempo_execucao = fim - inicio
    print(f"Tempo de execução de BFS: {tempo_execucao:.6f} segundos")

# Função principal
def main():
    grafo = Grafo()
    grafo.ler_grafo("grafo_6.txt")

    # Estudo de Caso 1 - alocacao de Memoria-----------------
    #estudo_de_caso_matriz(grafo)
    #estudo_de_caso_vetor(grafo)
    
    #Estudo de caso 2 - tempo de execucao
    grafo.calcular_vetor_adjacencia()
    teste_bfs_vetor(grafo)
    #grafo.calcular_matriz_adjacencia()
    #teste_bfs_matriz(grafo)

if __name__ == "__main__":
    main()
