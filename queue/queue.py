from node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    # Adiciona um novo elemento à fila
    def push(self, data):
        node = Node(data)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node
        self._size += 1

    # Retorna o primeiro da fila sem removê-lo
    def peek(self):
        if self._size > 0:
            node = self.first.data
            return node
        raise IndexError("The queue is empty")

    # Remove o primeiro elemento e o retorna
    def pop(self):
        if self._size > 0:
            node = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._size -= 1
            return node
        raise IndexError("The queue is empty")

    # Tamanho da fila
    def __len__(self):
        return self._size

    # Representação da fila
    def __repr__(self):
        if self._size > 0:
            string = ""
            node = self.first
            while node:
                string += "[ " + str(node.data) + " ]->"
                node = node.next
                if node is None:
                    string += "None"
            return string
        raise IndexError("The queue is empty")

    # Print do objeto
    def __str__(self):
        return self.__repr__()