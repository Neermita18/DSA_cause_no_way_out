class Node:
    def __init__(self, value):
        self.value= value
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_front(self, value):
        node= Node(value)
        node.next=self.head
        self.head=node
    def head_value(self):
        if self.head is None:
            return -1
        else:
            return self.head.value
    def insert_back(self, value):
        node= Node(value)
        if self.head is None:
            node.next= self.head
            self.head= node
            return node
        c= self.head
        while c.next:
            c=c.next
        c.next= node
    def get_last_value(self):
        
        if self.head is None:
            return -1
        
        current = self.head
        while current.next:
            current = current.next
        return current.value
        

list= LinkedList()
list.insert_front(8)
print(list.head_value())
list.insert_front(9)
print(list.head_value())
list.insert_back(10)
print(list.get_last_value())
print(list.head_value())