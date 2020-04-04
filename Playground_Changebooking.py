import mysql.connector
from mysql.connector import Error
import pandas as pd
from datetime import datetime


connection=mysql.connector.connect(host='localhost',username='root',password='Saisravan@25')
cursor=connection.cursor()
cursor.execute("USE ADMIN")

def Bookig(connection):

    time = datetime.now()
    current_time_now = time.strftime("%H:%M:%S")
    current_hour = int(current_time_now[0:2])
    current_minutes = int(current_time_now[3:5])

    select_query = pd.read_sql_query("select * from booking",connection)

    for i in select_query.itertuples():

        if current_hour - int(i[-1][0:2])>=1 and current_minutes>=int(i[-1][3:5]):
            update_query = "update {} set {} = 'Slot Available' where Location = '{}'".format(i[2], i[3], i[1])
            cursor.execute(update_query)
            cursor.execute('commit')
            delete_query = "DELETE * from booking where SLOT = '{}' and GAME = '{}'".format(i[3],i[2])
            cursor.execute(delete_query)
            cursor.execute('commit')
            print('Slot {} is now available for Booking for {}'.format(i[3],i[2]))

        elif current_hour - int(i[-1][0:2])>1:
            update_query = "update {} set {} = 'Slot Available' where Location = '{}'".format(i[2], i[3], i[1])
            cursor.execute(update_query)
            cursor.execute('commit')
            delete_query = "DELETE FROM booking where SLOT = '{}' and GAME = '{}'".format(i[3], i[2])
            cursor.execute(delete_query)
            cursor.execute('commit')

        else:
            pass
