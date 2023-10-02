from bibliotecaGrafos import *
import time

if __name__ == "__main__":
    
    grafo1 = Grafo()
    grafo1.ler_grafo("grafo1.txt")
    grafo1.escrever_informacoes("grafo1_info.txt")

    # Comparar desemprenho de quantidade de memoria pela matriz de adjacencia ou vetor de adjacencia
    print('% de memória RAM usada:', psutil.virtual_memory()[2])   
    print("Memória em GB: ", psutil.virtual_memory()[3] / 1000000000)

    opcao = escolher_representacao()
    if opcao == 1:
        representacao = grafo1.matriz_de_adjacencia()
    elif opcao == 2:
        representacao = grafo1.vetor_de_adjacencia()

    del(representacao)
    #2.Compare o desempenho em termos de tempo de execucao das duas representacoes do grafo para BFS

    #3.Compare o desempenho em termos de tempo de execucao das duas representacoes do grafo na DFS
    
    #4.Determinar o pai dos vertices

    #4.Determinar distancia dos pares abaixo:
    print("Estudo de caso 4:")
    print(f"Distancia do par de vértices (10,20): {grafo1.distancia(10, 20, 2)}.")
    print(f"Distancia do par de vértices (10,30): {grafo1.distancia(10, 30, 2)}.")
    print(f"Distancia do par de vértices (20,30): {grafo1.distancia(20, 30, 2)}.")

    # 7. Calcula o diametro aproximado
    diametro_aproximado = meu_grafo.calcular_diametro_aproximado()
    print(f"O diâmetro aproximado do grafo é {diametro_aproximado}.")