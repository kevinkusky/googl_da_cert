""" 
    Indexing / string slicing

    Indexing is 0 based and has a negative index to reverse search

    String Slicing takes up to 3 values => my_string[start : stop : step]

    where the stop is not inclusive
"""

MY_STRING = 'I am a string!'

print(MY_STRING[0])   # 'I'
print(MY_STRING[-1])  # '!'

# From index 1 to 4
print(MY_STRING[1:5])  # ' am '
# Implied start of index 0 to index 2
print(MY_STRING[:3])  # 'I a'
# From 3rd index from end to end
print(MY_STRING[-3:])  #  'ng!'
# From start to second index from end
print(MY_STRING[:-1])  #  'I am a string'

# pylint: disable=pointless-string-statement
"""
    Data Types and Structures

    List - mutable, ordered collection of items
        Useful methods: count, index, clear, sort, 

    Tuple - immutable sequence
        Useful for unpacking data or assigning multible variables
        Useful methods: count, index

    Dictionary - unordered, key(immutable) value pairs
        Useful methods: keys, values, items, del

    Sets - mutable unordered and unique structure with immutable elements
        intersection, union, difference, symmetric_difference
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

# List comprehension
example_comprehension = [x*2 for x in my_list if x < 20]

# Enumerate
def example_enumerate(itr):
    """enumerate allows you to track index with cooresponding element"""
    res = []
    for i, el in enumerate(itr):
        res.append(i, el)

    return res

# Zip and Unzip
cities = ['Paris', 'Lagos', 'Mumbai']
countries = ['France', 'Nigeria', 'India']
places = zip(cities, countries)

# the zipped object needs to be type cast to display other than memory 
print(places)  # <zip object at 0x7f24470b58c8>
print(list(places))  #[('Paris', 'France'), ('Lagos', 'Nigeria'), ('Mumbai', 'India')]

scientists = [('Nikola', 'Tesla'), ('Charles', 'Darwin'), ('Marie', 'Curie')]
# Splat operator unpacks/unzips
given_names, surnames = zip(*scientists)
print(given_names)  # ('Nikola', 'Charles', 'Marie')
print(surnames)  # ('Tesla', 'Darwin', 'Curie')

# Tuples
dollars, cents = 9, 22

knicks = [
    ('Jalen', 'pg', 11),
    ('Josh', 'sg', 3),
    ('Mikal', 'sf', 25),
    ('OG', 'pf', 8),
    ('Karl', 'c', 32)
]

# for name, position, number in knicks:
#     print(name)

def unpack_position(team):
    """example function"""
    result = []
    for name, position, number in team:
        result.append(f'Name: {name :>19} \nPosition: {position :>15}\n')
        # result.append('Name: {:>19} \nPosition: {:>15}\n'.format(name, position))

    return result


# Dictionaries

# Sets
s1 = {1, 2, 3, 5, 7, 11, 13, 17}
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Union
# print(s1.union(s2))
print(s1 | s2)

# Intersection
# print(s1.intersection(s2))
print(s1 & s2) # {1, 2, 3, 5, 7}

# difference
# print(s1.difference(s2))
print(s1 - s2) # {11, 13, 17}
print(s2 - s1) # {4, 6, 8, 9, 10}

# symmetric difference
# print(s1.symmetric_difference(s2))
print(s1 ^ s2) # {4, 6, 8, 9, 10, 11, 13, 17}
