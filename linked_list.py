
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
       def calculate(node):
           if node is None:
               return 0
           return node.data + calculate(node.next)
       return calculate(self.head)

    def recursive_reverse(self):
       def reverse(node, previous):
           if node is None:
               return previous
           next_node = node.next
           node.next = previous
           return reverse(next_node, node)
       self.head = reverse(self.head, None)

    def recursive_search(self, target):
        def find(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return find(node.next)
        return find(self.head)

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end="")
            current = current.next

        print ("None")