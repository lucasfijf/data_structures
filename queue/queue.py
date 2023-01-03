from node import Node

class Queue:
    def __init__(self):
        self.last = None

    # Verifica se a fila está vazia
    def check_empty(self):
        return self.last is None

    # Adiciona um novo elemento à fila
    def push(self, data):
        node = Node(data)
        node.next = self.last
        self.last = node

    # Retorna o primeiro da fila sem removê-lo
    def peek(self):
        if not self.check_empty():
            first = self.last
            while True:
                if first.next != None:
                    first = first.next
                else:
                    break
            return first.data
        raise IndexError("The queue is empty")

    # Remove o primeiro elemento e o retorna
    def pop(self):
        if not self.check_empty():
            first = self.last
            node = self.last
            while True:
                if first.next != None:
                    node = first
                    first = first.next
                else:
                    node.next = None
                    break
            return first.data
        raise IndexError("The queue is empty")

    # Representação da fila
    def __repr__(self):
        string = ""
        node = self.last
        if self.last != None:
            while True:
                string += "[" + str(node.data) + "] -> "
                if node.next != None:
                    node = node.next
                else:
                    string += "None"
                    break
        return string

    # Print do objeto
    def __str__(self):
        return self.__repr__()