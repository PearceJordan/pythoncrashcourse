# Go through existing to-dos, listing each one and asking if it's been completed.
# Remove completed to-dos.
# Ask if more to-dos are needed, and allow user to add more to-dos.

# write file
# print file 
# ask user which files have been completed
# detect the user input
# append list
# ask user if there are more to-dos
# detect user input
# append list

# Function-write-list

# Function-detect-userinput

# Function-remove-completed-todos

# Function-add-additional-todos
#def get_user_input():
    #valid_input = False
    #while not valid_input:
        #user_input = input("Add a new to-do item or type 'q' to quit out")
        #if user_input == "q" or user_input.isalpha():
            #valid_input = True
            #return(user_input)
        #else:
            #print("Please write a to-do list without special characters.")

    


# todos = input
# with open("todos.txt", "w") as f:
    # f.write(f"{todos}")

try: 
    with open("todos.txt", "r") as f:
        content = f.read()
        todo_list = content.split("\n")

except FileNotFoundError: 
    with open("todos.txt", "w") as f:
        f.write("")

remaining_to_do_list = []

for todo in todo_list:
    print(todo)
    user_input = input("Completed? (y/n)")
    if user_input != "y":
        remaining_to_do_list.append(todo)

while True:
    new_todo = input("Add a new to-do or press'q' to quit: ")
    if new_todo == "q":
        break
    else:
        remaining_to_do_list.append(new_todo)

with open("todos.txt", "w") as f:
    output = "\n".join(remaining_to_do_list)
    f.write(output)

# for loop through the list
    #with open("todos.txt", "r") as f:
        #content = f.read()
        #print(content.split("\n"))
    
    # ask the user if they completed one
        # if yes: remove it
    # else
        # if no: keep it

# while loop 
    # ask for more todos
    # input "q" quit with break
        # break
    # else 
        # add to todos

# write added todos to the file
