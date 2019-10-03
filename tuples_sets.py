# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# # Create tuple
# fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# # Single value needs trailing comma to be a tuple
# fruits2 = ('Apples',)
# print(fruits2, type(fruits2))

# # Get value
# print(fruits[1])

# # Can't change value
# # fruits[0] = 'Pears'

# # Delete tuple
# del fruits2
# print(fruits2)

# # Get length
# print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set, cant add twice
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)