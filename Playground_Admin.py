import mysql.connector
from mysql.connector import Error
import Playground_insertion

def create(cursor):

    mysql_database = 'CREATE DATABASE IF NOT EXISTS ADMIN'


    mysql_table = """CREATE TABLE IF NOT EXISTS Manager ( 
                                           Manager_Name varchar(255),
                                           username varchar(255) PRIMARY KEY,
                                           password varchar(255),
                                           password_type varchar(255) DEFAULT 'Default',
                                           Email_ID varchar(255),
                                           Location varchar(255)  references Location(Location)) """


    mysql_table_locations = """CREATE TABLE IF NOT EXISTS Location ( 
                                           Location varchar(255) PRIMARY KEY,
                                           Game_1 varchar(255) DEFAULT 'Cricket',
                                           Price_Cricket varchar(255),
                                           Game_2 varchar(255) DEFAULT '8_Ball_Pool',
                                           Price_8_Ball_Pool varchar(255),
                                           Game_3 varchar(255) DEFAULT 'Badminton',
                                           Price_Badminton varchar(255),
                                           Game_4 varchar(255) DEFAULT 'TT',
                                           Price_TT varchar(255)) """


    mysql_table_cricket = """CREATE TABLE IF NOT EXISTS cricket ( 
                                                   Location varchar(255)  references Location(Location),
                                                   SLOT_1_9AM_12PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_2_11PM_1PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_3_3PM_6PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_4_6PM_9PM varchar(255) DEFAULT 'Slot Available') """


    mysql_table_8_Ball_Pool = """CREATE TABLE IF NOT EXISTS 8_Ball_Pool ( 
                                                   Location varchar(255)  references Location(Location),
                                                   SLOT_1_9AM_12PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_2_11PM_1PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_3_3PM_6PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_4_6PM_9PM varchar(255) DEFAULT 'Slot Available') """


    mysql_table_Badminton = """CREATE TABLE IF NOT EXISTS Badminton ( 
                                                   Location varchar(255)  references Location(Location),
                                                   SLOT_1_9AM_11PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_2_11PM_1PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_3_1PM_3PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_4_3PM_5PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_5_5PM_7PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_6_7PM_9PM varchar(255) DEFAULT 'Slot Available') """

    mysql_table_TT = """CREATE TABLE IF NOT EXISTS TT ( 
                                                   Location varchar(255)  references Location(Location),
                                                   SLOT_1_9AM_11PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_2_11PM_1PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_3_1PM_3PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_4_3PM_5PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_5_5PM_7PM varchar(255) DEFAULT 'Slot Available',
                                                   SLOT_6_7PM_9PM varchar(255) DEFAULT 'Slot Available') """

    mysql_table_Booking = """CREATE TABLE IF NOT EXISTS Booking ( 
                                                   Location varchar(255)  references Location(Location),
                                                   GAME varchar(255),
                                                   SLOT varchar(255),
                                                   Booking_time varchar(255)) """

    mysql_table_user_details = """CREATE TABLE IF NOT EXISTS user_details ( 
                                                       Location varchar(255)  references Location(Location),
                                                       GAME varchar(255),
                                                       SLOT varchar(255)) """

    cursor.execute(mysql_database)
    print("Database created")
    cursor.execute('USE ADMIN')
    lst = [mysql_table,mysql_table_locations,mysql_table_cricket,mysql_table_8_Ball_Pool,mysql_table_Badminton,mysql_table_TT,mysql_table_Booking,mysql_table_user_details]
    for i in lst:
        cursor.execute(i)
    print("Tables has been created")

try:
    connection = mysql.connector.connect(host='localhost', username='root', password='Saisravan@25')
    cursor = connection.cursor()
except Error as e:
    print(e)

create(cursor)
Playground_insertion.values(cursor)
Playground_insertion.Location_insertions(cursor)
Playground_insertion.Game_insertions(cursor)
