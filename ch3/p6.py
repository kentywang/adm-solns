"""
Use a hash table, implementated as an array of FIFO queues (implemented by a linked list). Each index of the array
is a hash value based on the category of food (e.g. dairy, egg, apple) so you can get the oldest item for any food type.

fridge.store(egg1)
fridge.store(dairy1)
fridge.store(egg2)
assert fridge.get(Category.EGG) == egg1
assert fridge.get(Category.EGG) == egg2
assert fridge.get(Category.DAIRY) == dairy
"""
