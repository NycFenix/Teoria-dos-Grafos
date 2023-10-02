from bibliotecaGrafos import *
import time

if __name__ == "__main__":
    
    grafo1 = Grafo()
    grafo1.ler_grafo("grafo1.txt")
    grafo1.escrever_informacoes("grafo1_info.txt")
    tempo_total = 0
    for i in range(1, 100):
        tempo_inicial = time.time()
        grafo1.BFS(i, 2)
        tempo_final = time.time()
        tempo_total += (tempo_final - tempo_inicial)
        
    print("Tempo médio de execução da BFS: ", tempo_total/100)
    
