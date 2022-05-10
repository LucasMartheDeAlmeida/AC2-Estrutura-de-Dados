from queue import Empty
import re


class Node:
    def __init__(self, initData, prev, prox):
        self.data = initData
        self.prev = prev
        self.next = prox

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData
    
class ListaEnc:
    def __init__(self):
        self.header = Node(None,None,None)
        self.tail = Node(None,None,None)
        self.header.next = self.tail
        self.tail.prev = self.header
        self.size = 0

    def is_empty(self):
        return self.size == 0
    def __len__(self):
        return self.size

    def insert_between(self, item, predecessor,sucessor):
        newest = Node(item, predecessor, sucessor)
        predecessor.next = newest
        sucessor.prev = newest
        self.size += 1
        return newest

    def delete_node(self,Node):
        predecessor =  Node.prev
        sucessor = Node.next
        predecessor.next = sucessor
        sucessor.prev = predecessor
        self.size -= 1
        Node.prev = Node.next = Node.element = None

    def insere_inicio(self, data):
        self.insert_between(data, self.header, self.header.next)
    
    def insere_final(self,data):
        self.insert_between(data, self.tail.prev, self.tail)

    def remove_comeco(self):
        if self.is_empty():
            raise Empty('Lista vazia!')
        return self.delete_node(self.header.next)
    
    def remove_ultimo(self):
        if self.is_empty():
            raise Empty('Lista Vazia!')
        return self.delete_node(self.tail.prev)
    
    def print_list(self):
        temp = self.header.next
        X = []
        while temp.next != None:
            X.append(temp.data)
            temp = temp.next
        return X


L = ListaEnc()

print(L.is_empty())

L.insere_inicio(2)
L.insere_final(3)
L.insere_inicio(4)
L.insere_final(6)
L.insere_inicio(8)
L.insere_final(9)
L.insere_inicio(10)


print(L.print_list())
print(L.size)
print(len(L))
L.remove_comeco()
L.remove_ultimo()

print(L.print_list())
print(len(L))