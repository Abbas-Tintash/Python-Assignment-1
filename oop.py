class Todo_list():

    def display_mainmenu():
        print("\n\n\n\t*****************************************************")
        print("\t\t\t\tTo Do List")
        print("\t*****************************************************")
        print("\t1. View your To Do List.\n\t2. Add items in a list.\n\t   Update an activity from To Do List"
          "\n\t   Remove an item from a list.\n\t3. Press e for exit.")
        print("\t*****************************************************")
        print("Select any numerical value to perform an action.")

    def displayList():
        test_list1 = []
        test_list2 = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]
        # printing original lists
        print("Done Mark : " + str(test_list1))
        print("To Do List: " + str(test_list2))

    def add():
        test_list1 = []
        test_list2 = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]
        done = int(input("Total number of Done items from To Do list: "))
        while 0 < done:
                c = input("Mark done from To do List: ")
                test_list1.insert(done, test_list2.pop(test_list2.index(c)))
                done = done - 1
        print("To Done List: " + str(test_list1))
        print("The To do list Remaining: " + str(test_list2))
        print("remove an item from to do list:")
        c = int(input("Please Write the index value: "))

        test_list1.pop(c)
        print("Updated done list: " + str(test_list1))

        print("The To do list Remaining: " + str(test_list2))

        print("To Update on Specific index: ")
        c = int(input("Please Write the index value: "))
        d = (input("Item from Todo list :"))
        test_list1.insert(c, d)
        print("Updated done list: " + str(test_list1))
        for x in test_list1:
            print(x, "    Done")
        for z in test_list2:
            print(z, "    Remaining Task")

def keeplive():
    print("Do you wish to continue or Exist? \n Press c fo continue & e for exist")
    s = input()
    if s == 'c':
        main()
    elif s == 'e':
        exit()
    else:
        s = input()

def main():
    Todo_list.display_mainmenu()
    num = int(input())
    if num == 1:
        Todo_list.displayList()
        keeplive()
    elif num == 2:
        Todo_list.add()
        keeplive()
    elif num == 3:
        exit()
    else:
        print("Wrong input ")
main()
