
# Move one list element to another list
# Using pop() + index() + insert()

# initializing lists
test_list1 = []
test_list2 = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]

# printing original lists
print("Done Mark : " + str(test_list1))
print("To Do List: " + str(test_list2))
done = int(input("Total number of Done items from To Do list: "))
# Move one list element to another list
total = int(input("Total number of To Do List Activities: "))
while 0 < done:
    c = input("Mark done from To do List: ")
    res = test_list1.insert(done, test_list2.pop(test_list2.index(c)))
    done = done - 1
# Printing result
print("To Done List: " + str(test_list1))
print("The To do list Remaining: " + str(test_list2))
print("Do you want to add another item? press y for yes and n for No")
yes = input()
if yes == 'y':
    done = int(input("Total number of Done items from To Do list: "))
    while 0 < done:
        c = input("Mark done from To do List: ")
        test_list1.insert(done, test_list2.pop(test_list2.index(c)))
        done = done - 1
        print("To Done List: " + str(test_list1))
        print("The To do list Remaining: " + str(test_list2))
elif yes == 'n':
    exit()


