# add & update
# To do list is to meet with Friends
# simple display of list
class display_list:
    Friend_List = ["abbas", "Usama", "Mujtaba"]
    print(Friend_List)
    # simple display with loop
    Friend_List = ["abbas", "Usama", "Mujtaba"]
    for x in Friend_List:
        print(x)
# adding item in Friend_list
# This append function will help to enter item in the last of list
def append():
    Friend_List = ["abbas", "Usama", "Mujtaba"]
    Friend_List.append("Malik")
    print(Friend_List)
# Now you want to enter value in specific location
# this time insert function will help you to enter specific item
# on you desire index position. current item will move to very next index.
def insert():
   Friend_List = ["abbas", "Usama", "Mujtaba"]
   Friend_List.insert(1, "Imran Khan")
   print(Friend_List)
