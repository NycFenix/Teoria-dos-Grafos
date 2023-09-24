#Criação de um nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.prev = None
        
#Criação da Pilha
class Pilha:
    def __init__(self):
        self.head = Nodo("head")
        self.tamanho = 0
        
    def get_size(self):
        return self.tamanho
    
    def isEmpty(self):
        return self.tamanho == 0
        
    def push(self, valor):
        nodo = Nodo(valor)
        nodo.next = self.head.next
        self.head.next = nodo
        self.tamanho +=1
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Pilha vazia!")
        removido = self.head.next
        self.head.next = self.head.next.next
        self.tamanho -=1
        return removido.valor  
    
    
class Fila:
    def __init__(self):
        self.head = None
        self.last = None
        
    def enqueue(self, valor):
        if self.last is None:
            self.head = Nodo(valor)
            self.last = self.head
        else:
            self.last.next = Nodo(valor)
            self.last.next.prev = self.last
            self.last = self.last.next
    
    def dequeue(self):
        if self.head is None:
            return None
        else:
            removido = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return removido
        
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    