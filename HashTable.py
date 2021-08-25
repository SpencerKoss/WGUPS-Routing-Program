# Hash Table class
class HashTable:

    # Default size and values
    def __init__(self):
        self.size = 60
        self.table = [None] * self.size

    # This function is designed to insert a key value pair into the Hash Table
    def insert(self, key, value):   # Complexity O(1)
        hash_value = hash(key)  # Getting hash value
        key_value = [key, value]  # The key_value to insert into the Hash Table

        if self.table[hash_value] is None:  # Checking if cell is empty
            self.table[hash_value] = list([key_value])  # Creates a list and adds key_value pair
            return True
        else:
            return False

    # This function is designed to take in a key and return the correct value
    def get(self, key):     # Complexity O(n)
        hash_value = hash(key)  # Getting hash value, given the key
        if self.table[hash_value] is not None:  # Checking if the cell is populated
            for key_value in self.table[hash_value]:  # Iterating through the list of keys
                if key_value[0] == key:
                    return key_value[1]
        return None

    # This function is designed to remove a value given the key in the Hash Table
    def remove(self, key):      # Complexity: O(n)
        hash_value = hash(key)  # Assigning hash value

        if self.table[hash_value] is None:  # Checking if cell is empty
            return False

        for i in range(0, len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:  # Determining if keys match
                self.table[hash_value].pop(i)  # Popping the value at specified hash value in list of i
                return True

    # This function is designed to print the contents of the Hash Table
    def print(self):    # Complexity O(n)
        for item in self.table:  # Iterate through the Table
            if item is not None:
                print(str(item))
