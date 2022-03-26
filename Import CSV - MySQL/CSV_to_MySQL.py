import csv
import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', password='', database='people')
cursor = connection.cursor()


# CRUD goes inside here

def import_csv():
    # Read the file you want to import
    with open('pessoas.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        # Here you define the columns and their names, so it can be saved as a variable and imported automatically to MySQL
        column_one = input('column_1 name: ') # The column's names take the same name of the headers in the file
        column_two = input('column_2 name: ')
        column_three = input('column_3 name: ')
        # Make a loop to read all the lines
        for line in csv_reader:
            # These var defines where the data will be placed, according to its index number. Think of the index as a column
            locals()[column_one] = line[0]
            locals()[column_two] = line[1]
            locals()[column_three] = line[2]
            # Inside de loop, execute the SQL command and define the VALUES to the same column variables above.
            # It's always important to check the column names so the data is imported correctly.
            command = f'INSERT INTO register (people_name,people_age,people_email) VALUES ("{locals()[column_one]}","{locals()[column_two]}","{locals()[column_three]}")'
            cursor.execute(command)
            connection.commit()


import_csv()

cursor.close()
connection.close()

# improvements to be done

# make the user define which CSV file to be opened.
# Insert other commands like delete, update and read.
