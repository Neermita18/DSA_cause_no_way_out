class Node:
    def __init__(self, value):
        self.value= value
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
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
        
    def insert_optimal(self, value):
        node= Node(value)
        if self.head is None:
            self.head= node
            self.tail=node
            return node
        self.tail.next= node
        self.tail=node
        
        
    def get_last_value(self):
        
        if self.head is None:
            return -1
        
        current = self.head
        while current.next:
            current = current.next
        return current.value
    
    def delete(self,value):
        if self.head.value==value:
            self.head= self.head.next
            return self.head
        c= self.head
        while c.next:
            if c.next.value==value:
                c.next= c.next.next
                return
            c=c.next
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
list.delete(8)
list.get_values()
# list.insert_optimal(50)
# list.get_values()
# list.insert_optimal(49)
# list.get_values()