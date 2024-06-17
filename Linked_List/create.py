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
    def insert_at_k(self, value, k):
        node= Node(value)
        if self.head is None:
            self.head=node
            return node
        current= self.head
        for _ in range(k-1):
            current=current.next
        node.next= current.next
        current.next=node

            
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
    def get_values(self):
        if self.head is None:
            print(-1)
        c = self.head
        print("Linked List: ")
        print(c.value)
        while c.next:
            c= c.next
            print(c.value)
     

list= LinkedList()
list.insert_front(8)
print(list.head_value(),"\n\n")
list.insert_front(9)
print(list.head_value(),"\n\n")
list.insert_back(10)
print(list.get_last_value(),"\n\n")
print(list.head_value(),"\n\n")
list.get_values()
list.insert_at_k(4,2)
list.get_values()