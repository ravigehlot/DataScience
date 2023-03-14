"""
Data Structure: Lists

Lists can store a collection of items of any type and are mutable,
meaning you can add, remove or modify items in the list. 

Lists are created using square brackets.

Lists are great when you need to store a collection of related items,
like a list of names, or a list of numbers.

Lists are used whenever you need to maintain a sequence of elements.
"""

names = ['Ravi', 'Allison', 'Eva']

# Appends the string 'Zoey' to the end of names.
names.append('Zoey')

names.remove('Allison')

# Even though Allison was removed from the list
# the sequence of elements was maintained.
for name in names:
    print(names.index(name))