tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#try 1 and 2 as one function.
# define a function
# for loop for the tasks
# if tasks are true, put it into a list

def list_of_tasks(list,bool ):
    task_status = []
    for thingy in list:
        if thingy["completed"] == bool:
            task_status.append(thingy["description"])
        else:
            None
    return task_status

#completed tasks
print(list_of_tasks(tasks, True))

#uncompleted tasks
print(list_of_tasks(tasks, False))

#create function with one parameter
#define a empty list
#for loop to append description value to our list
#return it then print it

def task_descriptions_list(list):
    description_list = []
    for thingy in list:
        description_list.append(thingy["description"])
    return description_list

print(task_descriptions_list(tasks))

#Exercise 4
# define a function with 2 parameters (lists and time)
# define a list for tasks over certain time
# for loop to go through them
#with an if to check if it's over the length
#append to our list 
#return our list

def long_tasks(list,time):
    lengthy_list_of_items = []
    for thingy in list:
        if thingy["time_taken"] >= time:
            lengthy_list_of_items.append(thingy["description"])
    return lengthy_list_of_items

print(long_tasks(tasks, 30))

#5. print any task with a given description.
#define a function with two parameter, the task description
#for loop to go through the list
# if the task == description, return the list entry

def task_description(list,task_desc):
    for thingy in list:
        if task_desc == thingy["description"]:
            return thingy

print(task_description(tasks,"Walk Dog"))

# update completed if task is done from false to true
# defining a function with 2 parameters, list and description
# for loop and if statement to check if description is the same
# update completed status to True
#print the entry
print("Question 6")
def update_status(list,task_desc):
    for thingy in list:
        if task_desc == thingy["description"] and thingy["completed"] == False:
            thingy["completed"] = True
            return thingy

print(update_status(tasks,"Feed Cat"))

#add a new item to a list
#add in all the stuff to go with it

print("Question 7")

tasks.append(
    { "description": "Finish CODE!!", "completed": False, "time_taken": 120 },
)
print(tasks)

print("Question 8")

print("Menu:")
print("1: Display All Tasks")
print("2: Display Uncompleted Tasks")
print("3: Display Completed Tasks")
print("4: Mark Task as Complete")
print("5: Get Tasks Which Take Longer Than a Given Time")
print("6: Find Task by Description")
print("7: Add a new Task to list")
print("M or m: Display this menu")
print("Q or q: Quit")

# while loop
# user input is a number or M or Q
#take the input and return
#user_input = input("Choose an option from above ")

def menu_items(list):
    
    while True:
        user_input = input("Choose an option from above ")
        if user_input == "1":
            print(tasks)
        elif user_input == "2":
            print(list_of_tasks(tasks, False))
        elif user_input == "3":
            print(list_of_tasks(tasks, True))
        elif user_input == "4":
        #     print(list_of_tasks(tasks, True))
        # elif user_input == "5":
        #     print(list_of_tasks(tasks, True))
        # elif user_input == "6":
        #     print(list_of_tasks(tasks, True))
        else:
            return "Not an option"
#
print(menu_items(tasks))

# while (True):
#     line = input("Type something: ")
#     if (line.lower() == "q"):
#         break
#     print(f"You typed: {line}")