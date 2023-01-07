# Write a Python program to create a doubly linked list, append some items and iterate through the list (print forward)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __repr__(self):
        current_node = self.head
        outList = ''
        while current_node is not None:
            outList = outList + '<->' + str(current_node.data)
            current_node = current_node.next
        return outList

    def add_item(self, item):
        
        if self.head is None:
            self.head = Node(item)
        else:
            current_node = self.head
            while current_node.next:
                self.count += 1
                current_node = current_node.next
            current_node.next = Node(data=item)
            temp_current_node = current_node
            current_node = current_node.next
            current_node.prev = temp_current_node
            self.count += 1

    def __getitem__(self, index):
        if index > self.count:
            return "Index_out_of_range"
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data
    
    def __setitem__(self, index, new_val):
        if index > self.count:
            return "Index out of range"
        if index == 0:
            self.head.data = new_val
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            current_node.data = new_val
            
    def delete_first_item(self):
        if self.head.next is not None:
            self.head = self.head.next
        else:
            raise Exception("Empty list")


lList = LinkedList()
lList.add_item(50)
lList.add_item(30)
lList[1] = 66
lList.add_item(40)

print("Initial List", repr(lList))
