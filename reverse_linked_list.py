class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_to_front(self,element):
        node = Node(element)
        node.next = self.head
        self.head = node

    def print_elements(self):
        temp = self.head
        count = 1
        while temp is not None:
            print("Element {} is {}".format(count,temp.data))
            temp = temp.next
            count = count + 1

    def iterative_reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def recursive_reverse(self,node):
        if node is None:
            return None
        if node.next is None:
            return node
        node1 = self.recursive_reverse(node.next)
        node.next.next = node
        node.next = None
        return node1


if __name__ == '__main__':
    llist1 = LinkedList()
    llist1.push_to_front(20)
    llist1.push_to_front(4)
    llist1.push_to_front(15)
    llist1.push_to_front(85)
    llist1.push_to_front(10)
    llist1.print_elements()
    llist1.head=llist1.recursive_reverse(llist1.head)
    print("After Reversing the linked list Recursively")
    llist1.print_elements()

    #create another linked list
    llist2 = LinkedList()
    llist2.push_to_front(14)
    llist2.push_to_front(10)
    llist2.push_to_front(65)
    llist2.push_to_front(35)
    llist2.push_to_front(40)
    llist2.print_elements()
    print("After Reversing the linked list iteratively")
    llist2.iterative_reverse()
    llist2.print_elements()
