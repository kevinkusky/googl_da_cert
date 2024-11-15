""" 
    Indexing / string slicing

    Indexing is 0 based and has a negative index to reverse search

    String Slicing takes up to 3 values => my_string[start : stop : step]

    where the stop is not inclusive
"""

my_string = 'I am a string!'

print(my_string[0])   # 'I'
print(my_string[-1])  # '!'

# From index 1 to 4
print(my_string[1:5])  # ' am '
# Implied start of index 0 to index 2
print(my_string[:3])  # 'I a'
# From 3rd index from end to end
print(my_string[-3:])  #  'ng!'
# From start to second index from end
print(my_string[:-1])  #  'I am a string'

# pylint: disable=pointless-string-statement
"""
    Data Types and Structures

    List - mutable, ordered collection of items
        Useful methods: count, index, clear, sort, 

    Tuple - immutable sequence
        Useful for unpacking data or assigning multible variables
        Useful methods: count, index
"""
# Lists
my_list = [1, 5, 20, 25, 69]

# adds element to end of List
my_list.append(22)  # [1, 5, 20, 25, 69, 22]

# adds element to specific index
# List.insert(index, element)
my_list.insert(3, 2)  # [1, 5, 20, 2, 25, 69, 22]

# removes element from list
# List.remove(element)
# List.pop(index))
my_list.remove(25)  # [1, 5, 20, 2, 69, 22]
my_list.pop(4)  # 69 => returns removed element


# Tuples
dollars, cents = 9, 22

knicks = [
    ('Jalen', 'pg', 11),
    ('Josh', 'sg', 3),
    ('Mikal', 'sf', 25),
    ('OG', 'pf', 8),
    ('Karl', 'c', 32)
]

for name, position, number in knicks:
    print(name)
