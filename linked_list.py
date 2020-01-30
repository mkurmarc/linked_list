class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end oh the list'''
        if not isinstance(x, Node):
            x = Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            return "[" + to_print[:-2] + "]"
        return "[]"

    def add_to_start(self, x):
        '''add x to the left of the list making it the head'''
        old_head = self.head
        self.head = x
        self.head.next = old_head

    def create_node_list(self):
        node_list = []
        while not (self.head == None):
            node_list.append(self.head.__str__())
            self.head = self.head.next
        return node_list

    def search_val(self, x):
        '''return indices where x was found'''
        node_list = self.create_node_list()
        print(node_list)
        for index in range(len(node_list)):
            if str(x) == node_list[index]:
                return f"{x} found at index {index}"

    def remove_val_by_index(self, x):
        '''remove and return value at index x provided as parameter'''
        pass

    def length(self):
        '''return the length of the list, rep'd by the number of nodes'''
        pass

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        pass


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()

print(my_list)
my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(5)



node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
my_list.add_to_start(node6)
my_list.add_to_start(node7)
my_list.add_to_start(node8)


print(my_list.search_val(6))
print(my_list.search_val(7))
