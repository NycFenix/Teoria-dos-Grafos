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
    
    set
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
            removido = self.head.valor
            self.head = self.head.next
            self.head.prev = None
            return removido
        
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def __repr__(self):
        nodo_atual = self.head
        if nodo_atual is None:
            return "Fila vazia!"
        string_lista = ""
        while nodo_atual:
            string_lista += str(nodo_atual.valor) + "->"
            nodo_atual = nodo_atual.next
            
            
        return "| " + string_lista + " |"
    
    def uniao(self, item):
            if not self.esta_na_fila(item):
                self.enqueue(item)

    def esta_na_fila(self, valor):
        current = self.head
        while current:
            if current.valor == valor:
                return True
            current = current.next
        return False
    
fila = Fila()
fila.enqueue(6923)
fila.enqueue(100)
fila.enqueue(99)
fila.enqueue(8)
print(fila.head.valor)
print(fila)