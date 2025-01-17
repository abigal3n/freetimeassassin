import sqlite3

conn = sqlite3.connect("/home/galen/data/freetime_eliminator.db")

cursor = conn.cursor()

def minibox_manager(choice):
    if choice == 1:
        return

def getTaskID(tablename):
    tableRows = f"SELECT * FROM {tablename}"
    cursor.execute(tableRows)
    return(len(cursor.fetchall()))

#getTaskID("zombieapocalypse")

print("Do you have some freetime you would like to use wisely?\nWell never fear the FreeTimeAssassin is here!")
selection = int(input("Here you can input tasks or hobbies, assign them to projects, and randomly generate them as you please!\nWhat would you like to do?: \n1.) >Create a new task\n2.) >View current tasks\n3.) >Manage projects\n(input h for help)"))


if selection == "h" or selection == "help":
    print("coming soon...")
elif selection == 1:
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
elif selection == 2:
    generate = input("I am the generator (not ai though)... I can generate anything you like...\n1.) random task \n2.) project task \n3.) cant choose a project? i'll choose one for you! ")
elif selection ==3:
    print("Project Manager: You can...\n1.) Add new project\n2.) View existing projects\n3.) Edit Existing Projects")
# //cursor.execute('''CREATE TABLE IF NOT EXISTS '''
# )
# cursor.execute('''CREATE TABLE IF NOT EXISTS activity(id integer NOT NULL, type text NOT NULL, project text, name text NOT NULL)''');
display = input('what table do you want the tasks from?\n')
displaySQL = f"SELECT * FROM {display}"
cursor.execute(displaySQL)
result = cursor.fetchall()
print(result)

conn.commit()

conn.close()