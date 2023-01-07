# Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false

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

def searchItem(lList, item):
  current_node = lList.head
  while current_node is not None:
    if current_node.data == item:
          return True
    current_node = current_node.next
  return False
  
print('3', searchItem(lList, 3))
print('4', searchItem(lList, 4))
print('10', searchItem(lList, 10))
print('11', searchItem(lList, 11))
print('None', searchItem(lList, None))