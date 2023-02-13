# The point of this script is to make an easily interactive and updateable todo list by opening using hotkeys and taking user inputs to:
# View, Add, update, or delete stuff from the list. https://www.youtube.com/watch?v=AN3X59JIDqU
import mysql.connector
import os
#from dotenv import load_dotenv,find_dotenv

dataDict = {}
counter = 0

def dotenv_SQL_setup():
    #load_dotenv(find_dotenv())
    #passwrd= os.getenv('MYSQLPASSWORD')
    passwrd = "daphne99"
    dict = {
        'host': 'localhost',
        'database':'todo',
        'user' : 'root',
        'password': passwrd
    }
    database = mysql.connector.connect(**dict)
    #global Cursor
    Cursor = database.cursor()
    print("CONNECTION SUCCESSFUL")
    Cursor.execute("SELECT * FROM todolist")
    global dataDict, counter
    for x in Cursor:
        counter += 1
        dataDict[counter] = x[0]
    mains(Cursor,database)


def addto(Cursor, database):
    val = input("What would you like to add?\n")
    sql = "INSERT INTO todolist (item) VALUES (%s)"
    Cursor.execute(sql,[val])
    database.commit()
    global counter
    counter += 1
    dataDict[counter] = val
    return print("Item successfully added.")


def remove(Cursor, database):
    for y in dataDict:
         print(y, "\t" + dataDict[y])
    val = input("Which input would you like to remove? Type the associated index or '-all'\n")
    if val == '-all':
        for x in range(len(dataDict)):
            val = dataDict[x+1]
            sql = "DELETE FROM todolist WHERE (%s = item)"
            Cursor.execute(sql,[val])
            database.commit()
        print("Database Empty.")
        return
    else:
        sql = "DELETE FROM todolist WHERE (%s = item)"
        Cursor.execute(sql,[dataDict[int(val)]])
        database.commit()
        del dataDict[int(val)]
        return print("Item successfully removed.")
    

def show(Cursor):
    print("\n -----------------------------------")
    print("  ---------  TO DO LIST  ----------")
    print(" -----------------------------------")
    #SQL
    Cursor.execute("SELECT * FROM todolist")
    #Loop through database object and show results
    counter = 1
    emptyflag = True
    for x in Cursor:
        print(" \t",counter, "\t", x[0])
        counter += 1
        emptyflag = False
    if emptyflag:
        print("\t   List is Empty.")


def mains(Cursor,database):
    while True:
        cmd = input("\nEnter a command:\n")
        if cmd[0] == '-':
            cmd = cmd[1:]
        else:
            print("Invalid Command Argument. Missing '-'.\nPlease enter a command, if you need a list, type '-help'")
            continue
        if cmd == "add":
            addto(Cursor, database)
        elif cmd == "remove":
            remove(Cursor, database)
        elif cmd == "show":
            show(Cursor)
        elif cmd == "help":
            print("Valid Command Arguments:\n '-add': adds to the list\n '-remove': removes item from list\n\t'-all': removes all entries\n '-show': prints the list\n '-help': shows a list of commands\n '-exit' / '-quit': exits the program")
        elif cmd == "exit" or cmd == "quit":
            database.close()
            quit()
        else:
            print("Invalid Command Argument. If you need a list of valid command arguments, type '-help'")

if __name__ == "__main__":
    dotenv_SQL_setup()