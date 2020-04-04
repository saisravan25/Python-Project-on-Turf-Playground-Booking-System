import random
import string
import Playground_Email

def insertion(cursor,Manager_Name,username,password,Email_ID,Location):
    if Playground_Email.Email(Manager_Name,username,password,Email_ID):
        mysql_insert = """INSERT IGNORE into Manager (Manager_Name,username,password,Email_ID,Location) VALUES (%s,%s,%s,%s,%s)"""
        record = (Manager_Name, username, password, Email_ID, Location)
        cursor.execute(mysql_insert, record)
        cursor.execute('commit')
        print("Manager Details Inserted")

def Location_insertions(cursor):
    cursor.execute('USE ADMIN')
    mysql_insertion_1 = """INSERT IGNORE into Location (Location,Game_1,Price_Cricket,Game_2,Price_8_Ball_Pool,Game_3,Price_Badminton,Game_4,Price_TT) VALUES ("Whitefield","Cricket",2500,"8_Ball_Pool",1200,"Badminton",1000,"TT",800)"""
    mysql_insertion_2 = """INSERT IGNORE into Location (Location,Game_1,Price_Cricket,Game_2,Price_8_Ball_Pool,Game_3,Price_Badminton,Game_4,Price_TT) VALUES ("Marathalli","Cricket",2300,"8_Ball_Pool",1000,"Badminton",800,"TT",700)"""
    mysql_insertion_3 = """INSERT IGNORE into Location (Location,Game_1,Price_Cricket,Game_2,Price_8_Ball_Pool,Game_3,Price_Badminton,Game_4,Price_TT) VALUES ("HAL","Cricket",2200,"8_Ball_Pool",1100,"Badminton",900,"TT",600)"""
    lst = [mysql_insertion_1,mysql_insertion_2,mysql_insertion_3]
    for i in lst:
        cursor.execute(i)
    cursor.execute('commit')


def Game_insertions(cursor):
    cursor.execute('USE ADMIN')
    cursor.execute("INSERT IGNORE into Cricket (Location) VALUES ('Marathalli')")
    cursor.execute("INSERT IGNORE into Cricket (Location) VALUES ('Whitefield')")
    cursor.execute("INSERT IGNORE into Cricket (Location) VALUES ('HAL')")
    cursor.execute("INSERT IGNORE into 8_Ball_Pool (Location) VALUES ('Marathalli')")
    cursor.execute("INSERT IGNORE into 8_Ball_Pool (Location) VALUES ('Whitefield')")
    cursor.execute("INSERT IGNORE into 8_Ball_Pool (Location) VALUES ('HAL')")
    cursor.execute("INSERT IGNORE into Badminton (Location) VALUES ('Marathalli')")
    cursor.execute("INSERT IGNORE into Badminton (Location) VALUES ('Whitefield')")
    cursor.execute("INSERT IGNORE into Badminton (Location) VALUES ('HAL')")
    cursor.execute("INSERT IGNORE into TT (Location) VALUES ('Marathalli')")
    cursor.execute("INSERT IGNORE into TT (Location) VALUES ('Whitefield')")
    cursor.execute("INSERT IGNORE into TT (Location) VALUES ('HAL')")
    cursor.execute('commit')


def randompassword(stringLength=10):

    password_characters=string.ascii_letters+string.digits+'@'

    return ''.join(random.choice(password_characters) for i in range(stringLength))


def values(cursor):
    while True:
        Manager_Name = input("Enter name of the Manager : ")
        username = input("Enter username : ")
        password = randompassword()
        Email_ID = input("Enter Email_ID : ")
        Location = input("Enter the location : ")
        insertion(cursor,Manager_Name, username, password, Email_ID, Location)
        ch = input("Do you want to insert more records : y/n")
        if ch == 'N' or ch == 'n':
            return



