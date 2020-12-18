'''         ARTEM'S CSPT8 LECTURE 
https://www.youtube.com/watch?v=NwsLkmf6r0c&feature=youtu.be
            ARTEM'S CSPT11 LECTURE 
https://www.youtube.com/watch?v=StGch8xUmNQ&feature=youtu.be
'''
####            --------------------------------------------------------------
####                                HASH FUNCTIONS DAY 1 
####            --------------------------------------------------------------

# HASH FUNCTION
#  - Any string input ---> a specific number (within some range)
#  - Most Important:
#     - This function must be deterministic
#     - Same input will always return the same output
#     - 1 input for 1 output

# Example - Print out each character
def my_hash(c):
    # take every character in string, convert character to number
    # where do the numbers come from? ASCII Table ---> http://www.asciitable.com/
    # convert each character into UTF-8 numbers or unicode ---> modern/standard approach- more characters
        # https://www.utf8-chartable.de/unicode-utf8-table.pl?number=1024
    

    for char in c:
        print(char)

# This will print out each character, line by line
# my_hash('Boop the Snoot')

''' OUTPUT:
            B
            o
            o
            p

            t
            h
            e

            S
            n
            o
            o
            t
'''

# 2nd example - print out unicode numbers
def my_hash1(c):
    # convert string into UTF --> use encode()
    string_utf = c.encode() # returns an array

    for byte_char in string_utf:
        print (byte_char)

# my_hash1('Boop the Snoot')

''' OUTPUT 
            66
            111
            111
            112
            32
            116
            104
            101
            32
            83
            110
            111
            111
            116
'''


# 3rd example - to get 1 number as the sum of encoded string - also returning 32 bit number or less
def my_hash2(c, length_limit): # O(n) where n is length of string
    string_utf = c.encode()

    total = 0
    for char in string_utf:
        total += char
        # make hash function 32 bit
        total &= 0xffffffff # bitwise operation eight 'f' here (hexadecimal system) clamps big numbers down to 32 bits (16 f for 64 bits)
    
    # divide the total by the length limit but only return the remainder
    return total % length_limit # breaks down the large number into a range from 0-8 (the limit) 

# not sure why this is broken
# print(f'The sum of "Boop the Snoot" in Unicode:', my_hash2('Boop the Snoot'))

### CSPT11 3rd example
def hash_fn(s): # O(n) where n is length of string
    print(s)
    encoded_string = s.encode() # O(1)
    
    result = 0
    for byte_char in encoded_string:
        result += byte_char
    
    return result

### CSPT11 4th example

# getting an index
hash_array = [None] * 8
# map the results of function 'hash_fn' above to an index in some array
# use modulo to bind a number from 'hash_fn' to 0 --> length of the array

# set the hash value 
hash_value = hash_fn('banana')

# get the index with modulo
index = hash_value % len(hash_array)
print(index)

# set the index to a value
hash_array[index] = 'is yellow'
print(hash_array)





# print(hash_fn('apple'))
''' OUTPUT 
        530
'''


# ####            --------------------------------------------------------------            ####
# ####                                CREATE HASH TABLE                                     ####
# ####            --------------------------------------------------------------            ####

'''
Hash Function + An Array == HashTable

To insert a key and value to this HashTable
    - hash the key to convert it to a number
    - take that number and MOD it by the size of the HashTable
    - insert the VALUE into the index given by the MOD operation
'''

# hash table is an array :)
hash_table = [None] * 8 # eight elements of 'None'

# ADD items to hash table - use the my_hash2 function
# store the sum of the word to an element in the hash table
index = my_hash2('Boop', len(hash_table)) # 400 (sum of Boop) % 8 (length of table) = 0
# print(index)
''' OUTPUT 
            0
'''
hash_table[index] = 'Value for Boop'
# print(hash_table) 
''' OUTPUT 
            ['Value for Boop', None, None, None, None, None, None, None]
'''

# 2nd example - bound word to a number between 0-8 (length of the array)
index = my_hash2('the', len(hash_table)) # 400 (sum of the) % 8 (length of table) = 0
# print(index)
''' OUTPUT 
            1
'''
hash_table[index] = 'Value for the'
# print(hash_table) 
''' OUTPUT 
            ['Value for Boop', 'Value for the', None, None, None, None, None, None]
'''

# retrieve value/items from hash table
index = my_hash2('Boop', len(hash_table)) # storing
print(hash_table[index]) # retriving
''' OUTPUT 
            Value for Boop
'''


# RUNTIME of adding and retrieveing - O(n) since hash function is O(n) 


# ####            --------------------------------------------------------------            ####
# ####                                COLLISION
# ####            --------------------------------------------------------------            ####

# # make a collision
# index = my_hash2('apple', len(hash_table))
# hash_table[index] = 'Value for apple'
# # print(hash_table[index])
# print(index)

# index = my_hash2('card', len(hash_table))
# hash_table[index] = 'Value for card'
# # print(hash_table[index])
# print(index)
# print(hash_table)