'''         ARTEM'S CSPT8 LECTURE 
https://www.youtube.com/watch?v=lVZZiy6a1S4&feature=youtu.be
'''
####            --------------------------------------------------------------
####                                HASH FUNCTIONS DAY 2
####            --------------------------------------------------------------

# set up the limited hash table
hash_table = [None] * 8

# get hashed number
def my_hash(s):
    '''
    Take every character in the string and convert character to number.
    Convert each character into UTF-8 numbers
    '''
    string_uft = s.encode()

    total = 0

    for char in string_uft:
        total += char
        total &= 0xffffffff # limit total to 32 bits
    return total

# get index
def hash_index(key):
    # creates the hash
    hash_num = my_hash(key)
    # computes where the hashed number should go in table
    return hash_num % len(hash_table)


def put(key, val):
    # hash the key and get an index
    i = hash_index(key)
    # check if something already exists at that index
    if hash_index[i] != None:
        # give warning
        print(f'Collision Warning! Overwritting...{repr(hash_table[i])}!')
    # store the value in the array at the hashed index
    hash_table[i] = val


def get(key):
    # hash the key and get an index
    i = hash_index(key)
    # return the value from the array at that index
    return hash_table[i]


# put 2 items in table
put('Hello', 'Hello Value')
put('World', 'World Value')

print(hash_table)

# make a collision
put('foo', 'foo value')
print(hash_table)
# value = get('Hello')
# # OUTPUT: ['World Value', None, None, None, 'Hello Value', None, None, None]
# print(value)
# # OUTPUT: Hello Value



























































