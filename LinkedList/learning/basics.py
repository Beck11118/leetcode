class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #Initializing Next as null or None

# node1 = Node(1)
# print(type(node1))
# print(node1.next)

class LinkedList:
    def __init__(self):
        self.head = None #Initializing head as None
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="  -> ")
            current = current.next
        print("None")

    # Insertation at the beginning
    def push_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Deleting the Node
    def delete_node(self, data):
        temp = self.head
        # If key is head of list
        if temp is not None:
           if temp.data == data:
               self.head = temp.next
               temp = None
               return
        # if key is in the inside of the link
        while temp.next:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        # if linked list empty
        if temp == None:
            return
        
        # Linking previus node to the one which is linked to deleting one
        prev.next = temp.next
        temp = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

#Creating Nodes with Linked List
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

# Linking Nodes 
ll.head.next = second
second.next = third

# Inserting data to the beginning
ll.push_at_beginning(0)

ll.print_list()
# Deleting the Node which holdes the data 
# ll.delete_node(2)

ll.reverse()
print(ll.print_list())

