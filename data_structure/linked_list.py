from data_structure.linked_list_interface import iLinkedList


class LinkedList(iLinkedList):
    class Node:
        def __init__(self, data=None) -> None:
            self.data = data            
            self.next = None        

    def __init__(self, data=None) -> None:
        self.head = self.Node()
        self.length = 0
        if data is not None:
            self.add(data=data)
            
    
    def add(self, data: any):
        if self.length == 0:
            self.tail = self.Node(data)
            self.head.next = self.tail
        else:
            self.tail.next = self.Node(data)
            self.tail = self.tail.next
        self.length += 1

    def remove(self, index: int):
        if index >= self.length:
            raise IndexError("Invalid position.")
        aux = self.head.next
        count = 0
        while count < index - 1:
            aux = aux.next
            count += 1
        item = aux.next.data
        aux.next = aux.next.next
        self.length -= 1
        return item
    
    def insert(self, index: int, data: any):
        if index < 0 or index > self.length:
            raise IndexError("Invalid index.")
        if index == self.length:
            self.add(data=data)
        else:
            count = 0
            aux = self.head.next
            while count < index - 1:
                aux = aux.next
                count += 1
            temp = aux.next
            aux.next = self.Node(data)
            aux = aux.next
            aux.next = temp
            self.length += 1
    
    def puts(self):
        aux = self.head.next        
        while aux:
            print(f"[{aux.data}] -> ", end="")
            aux = aux.next
        print("[None]")
    
    def get_by_index(self, index: int):
        count = 0
        aux = self.head.next
        while count < index - 1:
            aux = aux.next
            count += 1
        return aux.data
