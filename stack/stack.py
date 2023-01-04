from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    # Retorna o topo da pilha sem removê-la
    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    # Adiciona um novo elemento à pilha
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self._size += 1

    # Remove o elemento do topo e o retorna
    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError("The stack is empty")

    # Representação da pilha
    def __repr__(self):
        string = ""
        node = self.top
        while node:
            string += "[ " + str(node.data) + " ]\n"
            node = node.next
        return string

    # Print do objeto
    def __str__(self):
        return self.__repr__()