"""
Recreate python dictionaries using data structures called hash tables
"""

MAX_HASH_TABLE_SIZE = 4096

data_list = [None] * MAX_HASH_TABLE_SIZE

assert len(data_list) == 4096
assert data_list[99] == None

def get_index(data_list, a_string):
        """_summary_
        """
        
        # Variable to store the result (updated after each iteration)
        result = 0
        
        for a_character in a_string:
            # Convert the character to a number (using ord)
            a_number = ord(a_character)
            # Update result by adding the number
            result += a_number
        
        # Take the remainder of the result with the size of the data list
        list_index = result % len(data_list)
        return list_index
    
assert get_index(data_list, '') == 0
assert get_index(data_list, 'Aakash') == 585
assert get_index(data_list, 'Don O Leary') == 941

class BasicHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size
     
    
    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = value
    
    
    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
        
    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = value

    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]
    
basic_table = BasicHashTable(max_size=1024)

assert len(basic_table.data_list) == 1024

# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')

# Find a value
assert basic_table.find('Hemanth') == '8888888888'

# Update a value
basic_table.update('Aakash', '7777777777')

# Check the updated value
assert basic_table.find('Aakash') == '7777777777'

# Get the list of keys
assert basic_table.list_all() == ['Aakash', 'Hemanth']    