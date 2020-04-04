import mysql.connector
from mysql.connector import Error
#import Playground_selection
import pandas as pd

connection = mysql.connector.connect(host='localhost', username='root', password='Saisravan@25')
cursor = connection.cursor()
cursor.execute("USE ADMIN")

def password_change(connection, cursor, username):
    upper_case = 0
    lower_case = 0
    digits = 0
    special_characters = 0

    username_select = pd.read_sql_query(
        "select Manager_Name,username,password,password_type from manager where username = %s",
        connection, params=(username,))

    if username_select.iloc[:, 3][0] == 'Default':
        Old_password = (username_select.iloc[:, 2][0])

        change_password = input('Do you want to change the password? : Y/N')

        if change_password == 'y' or change_password == 'Y':

            Old_Password_check = input('Please enter old password : ')

            if Old_Password_check == Old_password:

                new_password = input('Please enter new password : ')

                if len(new_password) < 6 or len(new_password) > 16:
                    print("length not matching")
                    exit(1)
                for x in new_password:
                    if x.isupper():
                        upper_case += 1
                    elif x.islower():
                        lower_case += 1
                    elif x.isdigit():
                        digits += 1
                    elif x in ('$', '@', '&'):
                        special_characters += 1
                    else:
                        print("Invalid Password")
                        exit(1)

                if upper_case >= 1 and lower_case >= 1 and digits >= 1 and special_characters >= 1:
                    update_password = (
                        "update manager set password = '{}',password_type = '{}' where username = '{}' and password_type='Default'".format(
                            new_password, 'Changed', username))
                    cursor.execute(update_password)
                    cursor.execute('commit')
                    # print(update_password)
                    print('Password has been changed Successfully')
                    print('Please try logging in after 2 minutes')
                    exit(1)

                else:
                    print('Password crieteria mismatch')
                    exit(1)

            else:
                print('Password not matching')
                exit(1)
        else:
            print('Please reset password inorder to proceed')
            exit(1)