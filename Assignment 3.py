"""
Recreate python dictionaries using data structures called hash tables

Inputs: 
Outputs: 
"""

class HashTable:
    def insert(self, key, value):
        """Insert a new key-value pair"""
        pass
    
    def find(self, key):
        """Find the value associated with a key"""
        pass
    
    def update(self, key, value):
        """Change the value associated with a key"""
        pass
    
    def list_all(self):
        """List all the keys"""
        pass
    
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