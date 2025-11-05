#define the class 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

#define the class for the singulary linked list SLL
class SLL:

    def __init__(self):
        self.head = None

        #implement the insertion method
    def insert(self, data):
        new_node = Node(data)

        if not self.head #list is empty
            self.head = new_node
        else:
            current = self.head
            
            while current.head


    
