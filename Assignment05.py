# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JTrinh, 05.12.2020, Added code to complete assignment 5 (steps 3 & 4)
# JTrinh, 05.15.2020, Added code to steps 5-7
# JTrinh, 05.15.2020, deleted excessive comments/alternative code; basic functional script
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
ToDoFile = open(objFile,"r")
for row in ToDoFile:
    t, p = row.split(",")
    dicRow = {"Task": t, "Priority": p.strip()}
    lstTable.append(dicRow)
print(lstTable)
ToDoFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("Current Data: ")
        for row in lstTable:
            print(row["Task"] + ','+ row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        print("Enter a task and level of priority:")
        strTask = input("Task: ").upper()
        strPriority = input("Priority (high, medium, low): ").lower()
        # dicRow = {"Task":strTask, "Priority":strPriority}
        lstTable.append({"Task": strTask, "Priority": strPriority})
        # lstTable += dicRow
        for row in lstTable:
            print(row["Task"] + ", " + row["Priority"])
        #want to input "Add more?" code
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strTask = input("Task to remove: ")
        if dicRow["Task"].lower() != strTask.lower():
            print("Row not found")
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)
                print("row removed")
                print("Remaining Tasks: ")
                for row in lstTable:
                    print(row['Task'] + ',' + row['Priority'])
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        ToDoFile = open(objFile, "w")
        for row in lstTable:
            ToDoFile.write(row["Task"] + "," + row["Priority"] + "\n")
        ToDoFile.close()
        print("Data Saved")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("The program has ended" + "\n")
        input("(Press Enter to Exit)")
        break  # and Exit the program
