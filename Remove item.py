# Python Remove List Items
# Remove Specified Item
# To remove item from a list we have 3 different ways
# The remove() method removes the specified item.


Friend_List = ["abbas", "Usama", "Mujtaba"]
Friend_List.remove("Usama")
print(Friend_List)
 # Usana will remove
#Remove Specified Index
#The pop() method removes the specified index.

# Remove the second item:

Friend_List = ["abbas", "Usama", "Mujtaba"]
Friend_List.pop(1)
print(Friend_List)



# if you do not specify the index, the pop() method removes the last item.

# Example
# Remove the last item:

Friend_List = ["abbas", "Usama", "Mujtaba"]
Friend_List.pop()
print(Friend_List)

# The del keyword also removes the specified index:

# Example
# Remove the first item:

Friend_List = ["abbas", "Usama", "Mujtaba"]
del Friend_List[0]
print(Friend_List)

# The del keyword can also delete the list completely.
#
# Example
# Delete the entire list:

Friend_List = ["abbas", "Usama", "Mujtaba"]
del Friend_List

# Clear the List The clear() method empties the list.
#The list still remains, but it has no content.

# Example
# Clear the list content:

Friend_List = ["abbas", "Usama", "Mujtaba"]
Friend_List.clear()
print(Friend_List)