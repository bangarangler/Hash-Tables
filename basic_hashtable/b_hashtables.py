

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        # can think of as Fixed lenght array
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return hash % max

# print(hash("Hllo World", 16))


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    temp = hash(key, hash_table.capacity)
    new_pair = Pair(key, value)
    if hash_table.storage[temp] is not None:
        if hash_table.storage[temp][key] is key:
            print("Overwriting ...")

    hash_table.storage[temp] = new_pair



# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    temp = hash(key, hash_table.capacity)
    if hash_table.storage[temp] is not None:
        hash_table.storage[temp] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    temp = hash(key, hash_table.capacity)
    if hash_table.storage[temp] is not None:
        return hash_table.storage[temp].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")
    hash_table_insert(ht, "hello", "world\n")

    hash_table_remove(ht, "line")
    # hash_table_remove(ht, "hello")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")

    # print(hash_table_insert(ht,"name", "jon"))
    print(ht.storage)
    print(ht.storage[9])

Testing()
