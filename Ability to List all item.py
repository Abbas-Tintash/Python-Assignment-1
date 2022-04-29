# Ability to list all the  items in the list.


# Now Adding value in the list Dynamically
# using insert
size = int(input("Please select your list size  "))
list = []
for i in range(0, size):
    j = int(input("List item  "))
    list.insert(i, j)
print(list)

# Now Adding value in the list Dynamically
# using append method
size = int(input("Please select your list size  "))
list = []
for i in range(0, size):
    j = int(input("List item  "))
    list.append(j)
print(list)