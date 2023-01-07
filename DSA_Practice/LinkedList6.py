# Write a Python program to delete the first item from a singly linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __repr__(self):
        current_node = self.head
        outList = ''
        while current_node is not None:
            outList = outList + '->' + str(current_node.data)
            current_node = current_node.next
        return outList

    def add_item(self, item):
        current_node = self.head
        while current_node.next:
            self.count += 1
            current_node = current_node.next
        current_node.next = Node(data=item)
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
head_node = Node(1)
first_node = Node(2)
second_node = Node(3)
third_node = Node(10)

lList.head = head_node
head_node.next = first_node
first_node.next = second_node
second_node.next = third_node
lList.add_item(50)

lList[1] = 66

print("Initial List", repr(lList))

lList.delete_first_item()

print(repr(lList))

lList.delete_first_item()
lList.delete_first_item()
lList.delete_first_item()

print(repr(lList))




