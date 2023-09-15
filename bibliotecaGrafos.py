import numpy as np

texto = open("entrada.txt", "r")
    
vertice = int(texto.readline())
linhas = texto.readlines()
grafo= []

for linha in linhas[0:]:
    grafo.append(linha.strip().split())

print("vertice:",vertice)
print("arestas:", grafo)
texto.close()

def recorrencia(verticeProcurado):
    recorrencia = 0
    for linha in grafo:
        for item in linha:
            if item == verticeProcurado:
                recorrencia += 1

    return recorrencia

    print("recorrencia do vertice:", recorrencia("3"))



# class Grafo:
#     def __init__(self, vertices, arestas):
#          self.vertices = vertices
#          self.arestas = arestas
      
        
        
    
#     def vetorDeAjacencia(self):
#         vetor = np.array([])
#         for vertice in range (1, self.vertices):
#             vetor.concatenate(vetor)
#             for linha in self.arestas:
#                 if str(vertice) in linha:
                    
         
#         for linha in self.arestas:

        
#     def getGrauMinimo(self):
        
#         for linha in self.arestas:
            
#     def getGrauMaximo(self):
        
#     def getGrauMedio(self):
    
#     def getMedianaDeGrau(self):
            
#     def getGrauMaximo(self):
        
#     def getGrauMedio(self):
    
#     def getMedianaDeGrau(self):
        
          
         
            


