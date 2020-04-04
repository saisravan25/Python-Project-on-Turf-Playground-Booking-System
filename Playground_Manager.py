import mysql.connector
from mysql.connector import Error
import Playground_password
import Playground_Changebooking
from datetime import datetime

connection = mysql.connector.connect(host='localhost', username='root', password='Saisravan@25')
cursor = connection.cursor()
cursor.execute("USE ADMIN")

cursor.execute("SELECT username,password FROM Manager")
result = cursor.fetchall()

time = datetime.now()
current_time = time.strftime("%H:%M:%S")

def login_manager(connection):

    username = input("Enter the Username:")
    Login = False

    for i in result:
        if i[0] == username:
            password = input("Enter the Password:")

            if i[1] == password:
                Playground_password.password_change(connection, cursor, username)
                Login = True
                check_manager = "select Location from manager where username = '{}'".format(username)
                cursor.execute(check_manager)
                location_request = (cursor.fetchone())
                location_manager = (location_request[0])
                cursor.execute('select * from user_details')
                user_request = cursor.fetchall()
                count = 0

                for request in user_request:
                    location_user = (request[0])
                    game_user = (request[1])
                    slot_user = (request[2])

                    if location_manager == location_user:
                        print('There is a Booking request for Bangalore Sports Club {} for {}'.format(location_user,slot_user))
                        set_booked = ("update {} set {} = '{}' where Location = '{}';".format(game_user, slot_user, 'Booked',location_user))
                        cursor.execute(set_booked)
                        cursor.execute('commit')
                        insert_time = "INSERT into {} (LOCATION,GAME,SLOT,Booking_time) VALUES ('{}','{}','{}','{}')".format('Booking', location_user, game_user, slot_user, current_time)
                        cursor.execute(insert_time)
                        cursor.execute('commit')
                        delete_user_details = "DELETE FROM user_details WHERE SLOT = '{}'".format(slot_user)
                        cursor.execute(delete_user_details)
                        cursor.execute('commit')
                        count += 1
                        print('{} has been booked - Location - {}'.format(slot_user, location_user))
                        Playground_Changebooking.Bookig(connection)

                else:
                    if count == 0:
                        print("No requests Available for location {}".format(location_user))
                        exit(0)
            else:
                print("Invalid Password")
                exit(0)
    else:
        if not Login:
            print("Invalid Username")
            exit(0)


login_manager(connection)