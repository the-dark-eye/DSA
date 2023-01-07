# Write a Python program to find the size of a singly linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def __repr__(self):
    current_node = self.head
    outList = ''
    while current_node is not None:
      outList = outList + '->' + str(current_node.data)
      current_node = current_node.next
    print(outList)
    
lList = LinkedList()
head_node = Node(1)
first_node = Node(2)
second_node = Node(3)
third_node = Node(10)

lList.head = head_node
head_node.next = first_node
first_node.next = second_node
second_node.next = third_node

# lList.__repr__()

def findsize(lList : LinkedList):
  count = 0
  current_node = lList.head
  while current_node is not None:
    count += 1
    current_node = current_node.next
  return count
  
print(findsize(lList))