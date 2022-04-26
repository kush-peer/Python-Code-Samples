# Node class
from xml.dom.minidom import Node


class Nodes:
    # Function to initialize the node object
    def __init__(self, data = None, next = None):
        self.data = data # Assign data  contain int, string, complex object
        self.next = None # Initialize next as null
    
    #linked list class
class LinkedList:
       # Function to initialize the Linked
    # List object
        def __init__(self):
            self.head = None

        def insert_at_beginning(self, data):
            new_node = Nodes(data, self.head)
            self.head = new_node
        
        def print(self):
            if self.head is None:
                print("List is empty")
                return
            
            itr = self.head
            llSTR=''
            while itr is not None:
                llSTR += str(itr.data) + "--> "
                itr = itr.next
                print(llSTR)
        
        def insert_at_end(self, data):
            if self.head is None:
                self.head = Node(data,None)
                return
            
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = Node(data,None)
        
        def insert_values(self,data_list):
            self.head = None
            for data in data_list:
                self.insert_at_end(data) 
           
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(3) 
    ll.insert_at_end(6)  
    ll.insert_values(["test","test34"])  
    ll.print()
    