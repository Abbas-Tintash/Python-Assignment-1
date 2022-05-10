# to Do List
class todo_list:
    My_list = ["Eat", "sleep", "Play", "Code", "R&D", "Discussion"]
    print("what have you done so far?\nPlease select a number from respective options")
    for x in range(0, 6):
        print(x, " ", (My_list[x]))
    y = int(input("Enter Number :"))

    if y == 0:
        print("you are done with Eat")
        done_list = []
        # res = test_list1.insert(4, test_list2.pop(test_list2.index(10)))

        My_list = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]
        res = done_list.insert(0, My_list.pop(My_list.index(1)))
        My_list.pop("Eat")
        print("you are done with Eat")
        print("Remaining to do list :", My_list)
        print("Done list :", done_list)
        # size = int(input("Please select your list size  "))
        # list = []
        # for i in range(0, size):
        #     j = int(input("List item  "))
        #     list.append(j)
        # print(list)

        # complete_List = []
        # complete_List.append("Eat")
        # print(complete_List)
        # print("your Remaining activities are ", My_list)
    elif y == 1:
        print("you are done with Sleep")
        My_list = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]
        My_list.remove("Sleep")
        print("your Remaining activities are ", My_list)
    elif y == 2:
        print("you are done with Play")
        My_list = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]
        My_list.remove("Play")
        print("your Remaining activities are ", My_list)
    elif y == 3:
        print("you are done with Code")
        My_list = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]
        My_list.remove("Code")
        print("your Remaining activities are ", My_list)
    elif y == 4:
        print("you are done with R&D")
        My_list = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]
        My_list.remove("R&D")
        print("your Remaining activities are ", My_list)
    elif y == 5:
        print("you are done with Discussion")
        My_list = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]
        My_list.remove("Discussion")
        print("your Remaining activities are ", My_list)
    else:
        print("wrong key")
# y = (input())
# print("wrong key")
