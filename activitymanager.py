import sqlite3

conn = sqlite3.connect("/home/galen/data/freetime_eliminator.db")

cursor = conn.cursor()

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

def getTaskID(tablename):
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

def taskCreator():
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

def displayTasks(specific):
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

conn.commit()

conn.close()