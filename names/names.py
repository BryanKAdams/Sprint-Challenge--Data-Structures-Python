import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# Put all of names two values in a binary search tree
# assign names2 to be a binary search tree with the first value of names_2
# as the head
names2 = BinarySearchTree(names_2[0])
# loop through the rest of the names and insert them to the tree
for name in names_2[1:]:
    names2.insert(name)



duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# instead of using a nested for loop, we'll just do a lookup using the
# function built into our bst for whether the bst contains our value/name
for name_1 in names_1:
    if names2.contains(name_1):
        duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
