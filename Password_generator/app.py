import mysql.connector
from module import *
import pandas as pd

# Layout
menu = {
    "1": 'Insert',
    "2": 'Read',
    "3": "Update",
    "4": "Delete",
    "5": "Close"
}


def layout():
    print("-----------------------------")
    print("     PASSWORD DATABASE")
    print("-----------------------------")
    print("-----------------------------")

    for k, v in menu.items():
        print(f'{k} - {v}')
    print("-----------------------------")


connection = mysql.connector.connect(host='localhost', user='root', password='1234', database='password_generator')
cursor = connection.cursor()


def create_account_password():
    account_name = input("Account: ")
    account_password = auto_password_generator()

    command = f'INSERT INTO Password_table (Account_name, User_password) VALUES ("{account_name}", "{account_password}")'
    cursor.execute(command)
    connection.commit()
    print(f"{account_name}'s password saved to the Database")
    return account_password


def read_account_password():
    command = f'SELECT * FROM Password_table'
    cursor.execute(command)
    result = cursor.fetchall()  # read database

    dataframe = pd.DataFrame(result, columns=['ID', 'ACCOUNT', 'PASSWORD'])
    print(dataframe)


def update_account_password():
    try:
        account_name = input('Account: ')
        account_password = auto_password_generator()
        command = f'UPDATE Password_table SET User_password = "{account_password}" WHERE Account_name = "{account_name}"'
        cursor.execute(command)
        connection.commit()  # Edit the database (create, update, delete)
        print('Password updated')
    except:
        print('Update failed')


def delete_account_password():
    account_name = input('Account: ')

    command = f'DELETE FROM Password_table WHERE Account_name = "{account_name}"'
    cursor.execute(command)
    connection.commit()  # Edit the database (create, update, delete)

    print('Account deleted')


# main code
def running():
    while True:
        layout()
        try:
            manual_input = int(input("Select: "))
            if manual_input == 1:
                create_account_password()
            elif manual_input == 2:
                read_account_password()
            elif manual_input == 3:
                update_account_password()
            elif manual_input == 4:
                delete_account_password()
            elif manual_input == 5:
                print("App closed")
                break
        except ValueError:
            print("Please, select a valid option.")


running()

cursor.close()
connection.close()

'''
This piece of code allows one to run a CRUD in a database allowing the user to perform actions such as: 
Create, delete and update accounts and passwords. I should be used alongside the module.py provided.

DBMS used - MySQL (script in the folder)

There are lots of improvements to be done. Be my guest!
'''
