class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.insert(0, item)

    def is_empty(self):
        return len(self.itens) == 0
    
    def desempilhar(self):
        if not self.is_empty():
            return f"O item: {self.itens.pop(0)} foi desempilhado"
        return None
    
    def topo(self):
        if not self.is_empty():
            return self.itens[0]
        return None
    
    def tamanho(self):
        return len(self.itens)
    
    def __str__(self):
        return str(self.itens)
    

pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
print(pilha.topo()) # 4
pilha.empilhar(5)
pilha.empilhar(6)
print(pilha)
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
print(pilha.topo()) # 3
print(pilha)