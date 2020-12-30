'''         ARTEM'S CSPT8 LECTURE 
https://www.youtube.com/watch?v=lVZZiy6a1S4&feature=youtu.be

             ARTEM'S CSPT11 LECTURE 
https://www.youtube.com/watch?v=DtOh5pObfl4&feature=youtu.be
'''
####            --------------------------------------------------------------
####                                HASH FUNCTIONS DAY 2
####            --------------------------------------------------------------

# START -------------------------------FROM CSPT11----------------------------
''' The best way to deal with collisions is to make hash tables contain Linked Lists '''

class LinkedListNode: # also called HashTableEntry
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    # def __str__(self):
    #     s = "Node with value {} and next node: {}.".format(self.value, self.next)
    #     return s


class HashTable:
    # make a hash array
    def __init__(self, capacity): 
        self.hash_array = [None] * capacity
        self.capacity = capacity
        self.number_of_items = 0 # helps with resizing


    def hash_fn(self, s):
        # convert string into UTF-8 (Unicode) representation
        encoded_string = s.encode() # O(1)
        result = 0
        # every character is now a number based off UTF-8 rules
        for byte_char in encoded_string:
            # simply add the numbers up to get sone single new number
            result += byte_char
        
        return result

    def hash_index(self,key): # O(n) n is size of string
        # get the key
        hash_value = self.hash_fn(key)
        # MOD the key based on the array
        index = hash_value % len(self.hash_array) # convert number to a new number from 0 -len(array)
        return index

    ### To insert a key and value to this hash_table
    # - hash the key to convert it to a number
    # - take that number and MOD it by the size of the hash_table
    # - insert he VALUE into the index given by the MOD operaton
    def insert_into_hash_table(self,key, value): # O(1)
        index = self.hash_index(key)
        # make a warning for collision
        if self.hash_array[index] is not None: # if there is a value at index
            # print(f'Collision Warning - {self.hash_array[index]} index was overwritten')
            # fix the collision with linked lists
            
            # search LinkedList for Node with same KEY as the one we want to insert
            # if it exists:
                # change the value of node
                # return

            # if it does NOT exist:
                # first item in hash_array is HEAD of linked list
                # create a new LinkedListNode and add to the HEAD of linked list
                # make the new entry the new HEAD
            pass
        self.hash_array[index] = LinkedListNode(key, value) # This is where the linked list is
        # don't need to return anything


    ### To retrieve a value given a specific key from a hash_table
    # - hash the key to convert it to a number
    # - use MOD(%) to find the index within the underlying array
    # - use this new index to find the value in the array
    def get_from_hash_table(self, key): # 0(1)
        index = self.hash_fn(key)
        
        # search/loop through LinkedList at hashed index
        # compare the key to search to the keys in the nodes
        # if it is found
            # return the value
        # if not found
            # return None
        return self.hash_array[index].value

    def delete(self, key):
        index = self.hash_index(key)
        # search through linked list until node is found
        # if found
            # delete node

        pass

    def resize(self):
        # create a blank new array with double original size
        # rehash all items - hash function has changed (capacity)
            # go through each slot in array
                # go through each item in every linkedlist in array
                    # rehash key in each item, store in new array
        
        # make new array the new storage

'''
                            When to resize the hashtable? - Depends on Load Factor

                                                Num of items added
                            Load Factor =  ---------------------------------
                                            Capacity = num of slots in array
                        
    If the Load Factor is greater than 0.7 (70%), then we should INCREASE the size of the hash table
    If the Load Factor is less than 0.2(20%), then we should DECREASE the size of the hash table

'''

print('----------------------------------------')
table = HashTable(8)
table.insert_into_hash_table('apple', '8/lb') # index 2
table.insert_into_hash_table('oranges', '10/lb') # index 7
table.insert_into_hash_table('grapes', '3/lb') # collision with apple index at 2
# print(table.get_from_hash_table('apple'))
print(table.hash_array)


### Review of LinkedList - end of Lecture/Bonus Material
# - Linked Lists are a collection of Nodes

class HashTableEntry: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    # structure of the linkedlist
    def __init__(self):
        self.head = None

    # find nodes
    def find(self, key):
        # grab the current node - to start this will be the head
        current_node = self.head

        # while the current node exists - meaning NOT empty
        while current_node is not None:
            # compare current_node with what key we are looking for
            if current_node.key == key: # if the node matches the key - return node
                return current_node
            
            current_node = current_node.next # if node does not match - move to next node is list
        
        return None # Will return None is node is NOT in list
            
    def insert_at_head(self, node):
        # need to point current head to new node and point new head to old head

        # set the node to current HEAD
        node.next = self.head
        # set the new HEAD to new node
        self.head = node

    def delete_node(self, key):
        # when deleting HEAD
        if key == self.head.key:
            # move the HEAD over since we are deleting current HEAD
            self.head = self.head.next
            return self.head
        # when deleting anything else in list
        # create two pointers
        pervious_node = None # None since we are just starting out, no pervious node yet
        current_node = self.head

        # traverse the linked list via current_node pointer unit we find the correct node to delete
        while current_node in not None:
            # loop until correct key is found
            if current_node.key == key:
                # when found - set pervious and current pointers to be the same
                pervious_node.next == current_node.next
                return current_node # return node that was deleted for reference
                # move pointers
                pervious_node = current_node # move pervious to the same place as current
                # then move current_node over one
                current_node = current_node.next







# END -------------------------------FROM CSPT11----------------------------


# # set up the limited hash table
# hash_table = [None] * 8

# # get hashed number
# def my_hash(s):
#     '''
#     Take every character in the string and convert character to number.
#     Convert each character into UTF-8 numbers
#     '''
#     string_uft = s.encode()

#     total = 0

#     for char in string_uft:
#         total += char
#         total &= 0xffffffff # limit total to 32 bits
#     return total

# # get index
# def hash_index(key):
#     # creates the hash
#     hash_num = my_hash(key)
#     # computes where the hashed number should go in table
#     return hash_num % len(hash_table)


# def put(key, val):
#     # hash the key and get an index
#     i = hash_index(key)
#     # check if something already exists at that index
#     if hash_index[i] != None:
#         # give warning
#         print(f'Collision Warning! Overwritting...{repr(hash_table[i])}!')
#     # store the value in the array at the hashed index
#     hash_table[i] = val


# def get(key):
#     # hash the key and get an index
#     i = hash_index(key)
#     # return the value from the array at that index
#     return hash_table[i]


# # put 2 items in table
# put('Hello', 'Hello Value')
# put('World', 'World Value')

# print(hash_table)

# # make a collision
# put('foo', 'foo value')
# print(hash_table)
# # value = get('Hello')
# # # OUTPUT: ['World Value', None, None, None, 'Hello Value', None, None, None]
# # print(value)
# # # OUTPUT: Hello Value
