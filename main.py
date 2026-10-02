from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    Linked_list = LinkedList()
    Linked_list.insert_at_front(40)
    Linked_list.insert_at_front(30)
    Linked_list.insert_at_front(20)
    Linked_list.insert_at_front(10)
    
    print("Linked List:")
    Linked_list.display()

    print("Sum of all nodes:", Linked_list.recursive_sum())

    target = 30
    print("Searching for", target, ":", Linked_list.recursive_search(target))
    