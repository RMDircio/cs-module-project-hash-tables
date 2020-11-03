class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # super function here
        self.capacity = capacity
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # use capacity as the max of the list
        return len(list(self.capacity))


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.

        load factor = num of elements in the hash table / num slots

        ---------------------------------------------------------------
         BELOW IS FROM LINK:https://www.d.umn.edu/~gshute/cs2511/slides/hash_tables/sections/slides/hashtable_operations/load_factor.xhtml
        Q: Average-case?

        A: Let
        n 	= 	Number of keys stored in T
        m 	= 	Number of slots in T
        α 	= 	n/m
        Note:

            α = average number of elements in a chain, or load factor
            α can be less than or greater than 1
            If m is proportional to n (that is, m is chosen as a linear function of n), then n = O(m).
            In that case,

            α = n/m = O(m)/m = O(1)

        
        ANOTHER GOOD LINK: https://programming.guide/hash-table-load-factor-and-capacity.html
        """
        
        # number of keys divided by the number of buckets (length of the capacity)
        
        # number of keys stored
        num_of_keys = len(list(self.key))
        
        # number of buckets
        num_of_buckets = self.get_num_slots

        # divide
        return self.num_of_keys / self.num_of_buckets

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # mari lecture
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
           did_add_new_node = linked_list.insert_at_head_or_overwrite(Node(HashTableEntry(key, value)))
           if did_add_new_node:
               self.num_elements += 1
        
        else:
            linked_list = LinkedList()
            linked_list.insert_at_head_or_overwrite(HashTableEntry(key, value)))
            self.table[hash_table] = linked_list
            self.num_elements += 1
        
        if self.get_load_factor() > 0.7:
            self.resize(self.get_num_slots() * 2 ) # num_slots used instead of capacity

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # mari lecture
        # get hash index
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_table]
            # use the delete method
            did_delete_node = linked_list.delete(HashTableEntry(key, None))
            if did_delete_node != None:
                self.num_elements -= 1
                if self.get_load_factor() < 0.2: # check for extra space
                    self.resize(self.get_num_slots() / 2 ) # cut the table in half
        else:
            print('Warning: node not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # mari lecture
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            node = linked_list.find(HashTableEntry(key, None))
            if node != None:
                return node.value.value # get the value from Node and then the value from HashTable Entry

        return self.table[self.hash_index(key)] # from mari lecture


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # mari lecture
        old_table = self.table
        self.table = [None] * int(new_capacity)
        self.num_elements = 0

        for element in old_table:
            if element == None:
                continue
            curr_node = element.head
            while curr_node != None:
                temp = curr_node.next
                curr_node.next = None
                hash_index = self.hash_index(curr_node.value.key)

                if self.table[hash_index] != None:
                    self.table[hash_index].insert_at_head(curr_node)
                
                else:
                    linked_list = LinkedList()
                    linked_list.insert_at_head_or_overwrite(curr_node)
                    self.table[hash_index] = linked_list

                    curr_node = temp
                    self.num_elements += 1 # not neecsary but the number of slots WILL change



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
