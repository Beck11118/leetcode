# Apple: Red
# Banana: Yellow
# Orange: Orange
# 2. Hash Function (Simple version) - NOOOOB
def simple_hash(key):
    
    # we are noob that is way our keys are string, Because we are using first letter's position (A=1, B=2)

    return ord(key[0]) % my_hash_table.size 
    """
    Apple: A -> 1
    Banana: B -> 2
    Orange: O -> 15 (Shit, it is not within the range of our bucket. we need to do something)
    % modula ensures that we are within bucket size and (Shit, collisins might happen)
    ord the function to get the ASCII value of first character in key 
    """

class HashTable:

    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    
    # 3. Insertation - Storing Key-Value Pairs:
    def insert(self, key, value):
        # Bro, Let's find some hash indecies for our new key-value pairs
        hash_index = simple_hash(key)
        self.buckets[hash_index].append((key, value))

    # 4. Retriving - Getting Values

    def get(self, key):
        hash_index = simple_hash(key)

        for bucket_pair in self.buckets[hash_index]:
            if bucket_pair[0] == key:
                return bucket_pair[1]
        return 'Not found'
    


# Hey Dude, Create a hash table with 4 buckets
my_hash_table = HashTable(4) 

# Lets store our couples:
my_hash_table.insert('Apple', 'Red')
my_hash_table.insert('Banana', 'Yellow')
my_hash_table.insert('Orange', 'Orange')

# print(my_hash_table.buckets)

print(my_hash_table.get('Apple'))

