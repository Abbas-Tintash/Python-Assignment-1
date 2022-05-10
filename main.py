# from Add_Del import display_list
# from List_all_Items import List_items_Dynamically
# from Remove_Items import Remove_List_Items



from Display import Dashboard
Dashboardobj = Dashboard
print(Dashboardobj.display())
from To_Do_List import todo_list
todo_listobj = todo_list
opt = int(input("Selected option "))
if opt == '1':
    print(todo_listobj.My_list)
elif opt == '2':
    print()


