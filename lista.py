class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaSimplesmenteEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self, valor):
        novo_no = Node(valor)
        if not self.head:
            self.head = novo_no
        else:
            no_atual = self.head
            while no_atual.proximo:
                no_atual = no_atual.proximo
            no_atual.proximo = novo_no

    def percorrer(self):
        valores = []
        no_atual = self.head
        while no_atual:
            valores.append(no_atual.valor)
            no_atual = no_atual.proximo
        return valores
    

lista = ListaSimplesmenteEncadeada()
lista.inserir(1)
lista.inserir('Israel')
lista.inserir('Sival')
lista.inserir(True)
lista.inserir([1,2])
lista.inserir(False)
print(lista.percorrer())


