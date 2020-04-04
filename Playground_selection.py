import mysql.connector
from mysql.connector import Error
import pandas as pd

connection = mysql.connector.connect(host='localhost', username='root', password='Saisravan@25')
cursor = connection.cursor()
cursor.execute("USE ADMIN")

def display_slot(connection):

    print('*** Welcome to Bagalore Sports Club ***','\n')
    location_user = input('Please Select a location : ')
    location_query = "select Game_1,Game_2,Game_3,Game_4 from location where Location = '{}'".format(location_user)
    print(location_query)
    cursor.execute(location_query)
    available_games = (cursor.fetchone())
    print('Available games as below : ')
    for games in available_games:
        print(games)

    game = input("Please select a Game : ")

    if game == 'cricket' or game == 'Cricket':
        data = pd.read_sql_query("select * from cricket where Location='HAL'", connection)
        display_function(data, connection, location_user, game,location_user)

    elif game == 'badminton' or game == 'Badminton':
        data = pd.read_sql_query("select * from Badminton where Location='HAL'", connection)
        display_function(data, connection, location_user, game,location_user)

    elif game == '8_ball_pool':
        data = pd.read_sql_query("select * from 8_ball_pool where Location='HAL'", connection)
        display_function(data, connection, location_user, game,location_user)

    elif game == 'tt' or game == 'TT':
        data = pd.read_sql_query("select * from TT where Location='HAL'", connection)
        display_function(data, connection, location_user, game,location_user)

    else:
        print("Invalid Game")
        exit(0)

def display_function(data, connection, location, game,location_user):

    columns = list(data.columns.values)
    print('\n', '***Available slots as below***', '\n')

    count = 1
    for availability, slot in enumerate(columns[1:]):
        if data[slot][0] == 'Slot Available':
            print(slot, ' - Press {} to book a slot'.format(count))
        count += 1

    Slot_number = int(input("Enter the slot need to be booked:"))

    if data.iloc[:, Slot_number][0] == 'Slot Available':

        insert_user_details = "INSERT into {} (Location,GAME,SLOT) VALUES ('{}','{}','{}')".format('user_details',location_user,game,columns[Slot_number])
        print('\n','Request has been accepted for Location - {} Slot - {}'.format(location_user,columns[Slot_number]))
        cursor.execute(insert_user_details)
        cursor.execute('commit')

    if data.iloc[:, Slot_number][0] != 'Slot Available':
        print("Slot Unavailable")

display_slot(connection)
