#!/usr/bin/env python

import sqlite3

conn = None
c = None
columns = ""

def mainMenu():
    print ("\nChoose an option below:\n")
    print ("\t1. Create a new database")
    print ("\t2. Edit an existing database")
    print ("\t3. Quit\n")

def connectToFile():
    global conn, c
    dbName = raw_input("Enter database name including '.db' extension: ")
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    print ("Connected to %s !" % dbName)

def makeColumns():
    global columns
    while True:
        colName = raw_input("Enter column name: ")
        colType = raw_input("Enter column type: ")
        newCol = colName + " " + colType  
        addAnother = raw_input("Add another column? y/n: ").lower()
        
        if "y" in addAnother:
            newCol += ", "
            columns += newCol
        else:
            columns += newCol
            break
    
    return columns

def createTable():
    global c, columns
    tableName = raw_input("Enter a table name: ")
    makeColumns()
    c.execute("CREATE TABLE if not exists " + tableName + " (" + columns + ")")

def createNew():
    connectToFile()
    createTable()

while True:
    mainMenu()
    choice = int(raw_input("> "))

    if choice == 1:
        createNew()
    
    elif choice == 2:
        # editExisting()
        pass
    
    elif choice == 3:
        break


