from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    # Percorre a lista até o index
    def __getnode(self, index):
        node = self.head
        for i in range(index):
            if node:
                node = node.next
            else:
                raise IndexError("List Index Out of Range")
        return node

    # Insere um elemento a lista no index dado
    def insert(self, data, index):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self.__getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    # Remove o elemento no index dado
    def remove(self, index):
        node = self.__getnode(index)
        if self._size > 0:
            if index == 0:
                self.head = node.next
                self._size -= 1
                return node.data
            else:
                pointer = self.__getnode(index - 1)
                pointer.next = node.next
                self._size -= 1
                return node.data
        raise IndexError("The list is empty")

    # Tamanho da lista
    def __len__(self):
        return self._size

    # Representação da lista
    def __repr__(self):
        if self._size > 0:
            string = ""
            node = self.head
            while node:
                string += "[ " + str(node.data) + " ]->"
                node = node.next
                if node is None:
                    string += "None"
            return string
        raise IndexError("The list is empty")

    # Print do objeto
    def __str__(self):
        return self.__repr__()