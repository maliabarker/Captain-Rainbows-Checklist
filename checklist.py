checklist = list()

# CREATE
def create(item):
    checklist.append(item)
    #Create item here

# READ
def read(index):
    return checklist[index]
    #Read code here

# UPDATE
def update(index, item):
    checklist[index] = item
    #Update code here

# DESTROY
def destroy(index):
    checklist.pop(index)
    #Destroy code here

# LIST
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1
    #code to list all items in list

# COMPLETE
def mark_completed(index):
    item = checklist[index]
    update(index, "√" + item)
    #Marks an item as completed

def unmark_completed(index):
    item = checklist[index]
    unmarked_item = item.replace("√", "")
    update(index, unmarked_item)

# USER INPUT
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

# SELECT FUNCTION
def select(function_code):
    # Create item
    if function_code == "A":
        item = user_input("What item would you like to add to the list? >")
        create(item)

    # Read item
    elif function_code == "R":
        index = user_input("What index would you like to read? >")
        if int(index) < len(checklist):
            read(int(index))
        else:
            print("Index does not exist, please try again")
        # Remember that item_index must actually exist or our program will crash.

    elif function_code == "U":
        index = user_input("What is the index number of the item you would like to update? >")
        if int(index) < len(checklist):
            item = user_input("Please input the updated item >")
            update(int(index), item)
        else:
            print("Index does not exist, please try again")

    elif function_code == "D":
        index = user_input("What is the index of the item you would like to remove from the list? >")
        if int(index) < len(checklist):
            destroy(int(index))
        else:
            print("Index does not exist, please try again")

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "M":
        index = user_input("What is the index of the item you would like to mark as completed? >")
        if int(index) < len(checklist):
            mark_completed(int(index))
        else:
            print("Index does not exist, please try again")

    elif function_code == "UM":
        index = user_input("What is the index of the item you would like to umark? >")
        if int(index) < len(checklist):
            unmark_completed(int(index))
        else:
            print("Index does not exist, please try again")

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True


# TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST 
def test():
    # Add your testing code here
    create("purple sox")
    create("red cloak")
    create("blue shoes")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # mark_completed(0)

    # print(read(0))

    # # Call your new function with the appropriate value
    # select("C")
    # # View the results
    # list_all_items()
    # # Call function with new value
    # select("R")
    # # View results

    # user_value = user_input("Please Enter a value:")
    # print(user_value)


    # list_all_items()
    # # Continue until all code is run

test()

running = True
while running:
    selection = user_input(
        "Press A to add to the list, R to read from the list, U to update an item in the list, D to remove an item from the list, P to display list, M to mark an item as completed, and UM to un-mark an item as completed. Press Q to quit >")
    running = select(str.upper(selection))