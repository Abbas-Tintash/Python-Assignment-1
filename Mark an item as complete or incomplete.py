# to Do List
My_list = ["Eat", "sleep", "Play", "Code", "R&D", "Discussion"]
print("what have you done so far?\nPlease select a number from respective options")
for x in range(0, 6):
    print(x, " ", (My_list[x]))
y = int(input("Enter Number :"))
if y == 0:
        print("you are done with Eat")
        My_list = ["Eat", "Sleep", "Play", "Code", "R&D", "Discussion"]
        My_list.remove("Eat")
        print("your Remaining activities are ", My_list)
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