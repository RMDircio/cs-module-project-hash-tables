'''         ARTEM'S CSPT8 LECTURE 
https://www.youtube.com/watch?v=NwsLkmf6r0c&feature=youtu.be
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

# Example
def my_hash(c):
    # take every character in string, convert character to number
    # where do the numbers come from? ASCII Table ---> http://www.asciitable.com/
    # convert each character into UTF-8 numbers or unicode ---> modern/standard approach- more characters
        # https://www.utf8-chartable.de/unicode-utf8-table.pl?number=1024
    

    for char in c:
        print(char)

# my_hash('Boop the Snoot')


# 2nd example
def my_hash1(c):
    # convert string into UTF --> use encode()
    string_utf = c.encode() # returns an array

    for char in string_utf:
        print (char)

# my_hash1('Boop the Snoot')


# 3rd example - to get 1 number as the sum of encoded string - also returning 32 bit number or less
def my_hash2(c, length_limit):
    string_utf = c.encode()

    total = 0
    for char in string_utf:
        total += char
        # make hash function 32 bit
        total &= 0xffffffff # bitwise operation eight 'f' here (hexadecimal system) clamps big numbers down to 32 bits (16 f for 64 bits)
    
    # divide the total by the lengtt limit but only return the remainder
    return total % length_limit # breaks down the large number into a range from 0-8 (the limit) 

# print(f'The sum of "Boop the Snoot" in Unicode:', my_hash2('Boop the Snoot'))


####            --------------------------------------------------------------            ####
####                                CREATE HASH TABLE
####            --------------------------------------------------------------            ####


# hash table is an array :)
hash_table = [None] * 8 # eight elements of 'None'

# ADD items to hash table - use the my_hash2 function
# store the sum of the word to an element in the hash table
index = my_hash2('Boop', len(hash_table)) # 400 (sum of Boop) % 8 (length of table) = 0
# print(index)

hash_table[index] = 'Value for Boop'
# print(hash_table) # OUTPUT: ['Value for Boop', None, None, None, None, None, None, None]


# 2nd example
index = my_hash2('the', len(hash_table)) # 400 (sum of th) % 8 (length of table) = 0
# print(index) # OUTPUT: 1
hash_table[index] = 'Value for the'
# print(hash_table) # OUTPUT: ['Value for Boop', 'Value for the', None, None, None, None, None, None]


# retrieve value/items from hash table
index = my_hash2('Boop', len(hash_table))
# print(hash_table[index])

# RUNTIME of adding and retrieveing - O(n) since hash function is O(n) 


####            --------------------------------------------------------------            ####
####                                COLLISION
####            --------------------------------------------------------------            ####

# make a collision
index = my_hash2('apple', len(hash_table))
hash_table[index] = 'Value for apple'
# print(hash_table[index])
print(index)

index = my_hash2('card', len(hash_table))
hash_table[index] = 'Value for card'
# print(hash_table[index])
print(index)
print(hash_table)