# Write a Python program to print a given doubly linked list in reverse order

from audioop import reverse
from threading import currentThread


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
            self.count += 1
        else:
            current_node = self.head
            while current_node.next:
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
    
    # 50<->30<->40<->70<->80<->None
    # 80<->70<->40<->30<->50<->None
     
    def reverse(self):
        
        current_node = self.head
        previous_node = None
        while current_node:
            # 30 | 40 | 70 | 80 | None
            temp_next_node = current_node.next
            # 50 -> None | 30 -> 50 | 40 -> 30 | 70 -> 40 | 80 -> 70
            current_node.next = previous_node
            # 50 | 30 | 40 | 70 | 80
            previous_node = current_node
            # 30 | 40 | 70 | 80 | None
            current_node = temp_next_node
        self.head = previous_node
            
            
            
lList = LinkedList()
lList.add_item(50)
lList.add_item(30)
lList.add_item(40)
lList.add_item(70)
lList.add_item(80)

print("Initial List", repr(lList))

lList.reverse()

print(repr(lList))


# def reverse_print_lList(lList):
#     current_node = lList.head
#     while current_node.next:
#         current_node = current_node.next
#     while current_node is not None:
#         print(current_node.data)
#         current_node = current_node.prev
#     # print(current_node.data)

# reverse_print_lList(lList)
