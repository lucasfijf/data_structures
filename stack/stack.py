from node import Node

class Stack:
    def __init__(self):
        self.top = None

    # Verifica se a pilha está vazia
    def check_empty(self):
        return self.top is None

    # Retorna o topo da pilha sem removê-la
    def peek(self):
        if not self.check_empty():
            return self.top.data
        raise IndexError("The stack is empty")

    # Adiciona um novo elemento à pilha
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    # Remove o elemento do topo e o retorna
    def pop(self):
        if not self.check_empty():
            node = self.top
            self.top = self.top.next
            return node.data
        raise IndexError("The stack is empty")

    # Representação da pilha
    def __repr__(self):
        string = ""
        node = self.top
        while node:
            string = string + str(node.data) + "\n"
            node = node.next
        return string

    # Print do objeto
    def __str__(self):
        return self.__repr__()