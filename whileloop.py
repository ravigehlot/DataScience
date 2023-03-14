"""
Python has two different types of loops:
    - for loop
    - while

The following statements can be used:
    - break
    - countinue
"""

# while loop, index starts at zero.
numbers = [1,2,3,4,5]

count = 0
while count < len(numbers):
    print(numbers[count])
    count += 1

# the count is five.

print('------------------------------------------------------------')

# while loop, using break.
# break is used to exit out of the loop.
numbersEmpty = []

count = 0
while count <= len(numbersEmpty):
    if count == 0:
        print('Break out of this loop.')
        break