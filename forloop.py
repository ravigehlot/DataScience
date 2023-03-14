"""
Python has two different types of loops:
    - for loop
    - while

The following statements can be used:
    - break
    - countinue
"""

# For loop
numbers = [1,2,3,4,5]

for item in numbers:
    print(item)

print('------------------------------------------------------------')

# while loop, using continue.
# continue is used to skip current block.

names = ['Ravi', 'Allison', 'Eva']

for name in names:
    if name != 'Allison':
        print(name)
        continue