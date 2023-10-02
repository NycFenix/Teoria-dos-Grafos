from bibliotecaGrafos import *
import time

if __name__ == "__main__":
    
    grafo1 = Grafo()
    grafo1.ler_grafo("grafo1.txt")
    grafo1.escrever_informacoes("grafo1_info.txt")
    
    print(grafo1.distancia(10, 20, 2))
    print(grafo1.distancia(10, 30, 2))
    print(grafo1.distancia(20, 30, 2))