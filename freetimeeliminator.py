import sqlite3
conn = sqlite3.connect("/home/galen/data/freetime_eliminator.db")

cursor = conn.cursor()

def minibox_manager(choice):
    if choice == 1:
        return

def getActivityID(tablename):
    tableRows = f"SELECT * FROM {tablename}"
    cursor.execute(tableRows)
    return(len(cursor.fetchall()))

def displayTables():
    getTables = f"SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(getTables)
    print(str(cursor.fetchall()))

def returnTables():
    tables = f"SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(tables)
    tables = cursor.fetchall()
    return [table[0] for table in tables]

def activityCreator():
    task = input("you have chosen to add a task: \nTask Name: ")
    taskcat = input("what kind of task is it?")
    minutes = int(input("How many minutes will it take?"))
    tableCreate = f"CREATE TABLE IF NOT EXISTS {taskcat}(id integer NOT NULL, name text NOT NULL, minutes integer NOT NULL)"
    cursor.execute(tableCreate)
    taskID = getTaskID(taskcat) + 1
    addTask = f"INSERT INTO {taskcat} (id, name, minutes) VALUES (?, ?, ?)"
    cursor.execute(addTask, (taskID, task, minutes))
    taskCount = getTaskID(taskcat)
    print("There are now " + str(taskCount) + " tasks in the table " + taskcat)
#getTaskID("zombieapocalypse")

def sanitaryInput(question):
    while True:
        output = input(str(question))
        try:
            if not output.isalnum():
                raise ValueError("Don't try to inject me! >:(")
            else:
                return output
        except ValueError as ve:
            print(""+str(ve))

def displayActivities(specific):
    if specific:
        while True:
            try:
                # while True:
                #     display = input('what table do you want the tasks from?\n')
                #     try:
                #         if not display.isalnum():
                #             raise ValueError("dont try to inject me >:(")
                #         break
                #     except ValueError as ve:
                #         print(""+str(ve))
                display = sanitaryInput('What table do you want the tasks from?\n')
                displaySQL = f"SELECT * FROM {display}"
                cursor.execute(displaySQL)
                result = cursor.fetchall()
                print(str(result) + "\n")
                break
            except sqlite3.Error as e:
                print("" + str(e))
    else:
        print("im supposed to display all tables and their options")
        tableList = returnTables()
        for tableName in tableList:
            print(tableName)
            displayTables = f"SELECT * FROM {tableName}"
            cursor.execute(displayTables)
            print(str(cursor.fetchall()) + "\n")

print("Hello there! Do you have some free time you'd like to get rid of? Well never fear, the FreeTimeAssassin is here!")

while True:

    selection = input("What would you like to do? (enter h for help and e for exit)\n1.) Spend some time (generate a task)\n2.) Manage Tasks\n3.) Manage Task Categories\n")


    if selection == "h" or selection == "help":
        print("coming soon...")
    elif selection == "e" or selection == "exit":
        print("exiting now...")
        break
    elif int(selection) == 1:
        generate = input("I am the generator (not ai though)... I can generate anything you like...\n1.) random task \n2.) project task \nWhat would you like?\n")
    elif int(selection) == 2:
        option = input("This is the task manager!\nWhat would you like to do?\n1.) Display Current Tasks \n2.) Add Task\n3.) Delete Task ")
        if int(option) ==   1:
            specific = True
            while True:
                check = input("Did you have a specific category in mind? (Y/n)(Enter L to list categories)")
                if check == "L":
                    displayTables()
                elif check == "y":
                    displayActivities(specific)
                    break
                else:
                    specific = False
                    displayActivities(specific)
                    break
        if int(option) == 2:
            activityCreator()
    elif int(selection) ==3:
        print("Project Manager: You can...\n1.) Add new project\n2.) View existing projects\n3.) Edit Existing Projects")
    elif selection == "e" or selection == "exit":
        print("exiting now...")
        break
    else:
        print("sorry I dont understand")
    # //cursor.execute('''CREATE TABLE IF NOT EXISTS '''
    # )
    # cursor.execute('''CREATE TABLE IF NOT EXISTS activity(id integer NOT NULL, type text NOT NULL, project text, name text NOT NULL)''');
    # display = input('what table do you want the tasks from?\n')
    # displaySQL = f"SELECT * FROM {display}"
    # cursor.execute(displaySQL)
    # result = cursor.fetchall()
    # print(result)

conn.commit()

conn.close()