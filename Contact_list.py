# Contact list Dictionary
phone_list = {
}


# Main Functions

def add_contact():
    name = str(input('Name: '))
    number = str(input('number: '))
    phone_list.update({name: number})
    return print(f'You added {name} to your Contact list.')


def delete_contact():
    name = str(input('Name: '))
    phone_list.pop(name)
    return print(f'You deleted {name} from your contact list.')


def update_contact():
    name = str(input('Name: '))
    number = str(input('number: '))
    phone_list.update({name: number})
    return print(f'You updated {name} in your Contact list.')


options = ('Add', 'Delete', 'Update', 'View', 'Leave')

# Main code
print('--------- CONTACT LIST ---------')
for i in options:
    print(f'{i}')
print('--------------------------------')

# While structure to loop the code and Conditional Statements to get the funcions 

while True:
    user_input = input('What would you like to do: ')
    if user_input == "Add":
        print('---------Add---------')
        add_contact()
        print('---------------------')
    elif user_input == 'View':
        print('---------View---------')
        for i in phone_list:
            print(f'{i}: {phone_list[i]}')
        print('----------------------')
    elif user_input == "Delete":
        print('---------Delete---------')
        delete_contact()
        print('------------------------')
    elif user_input == "Update":
        print('---------Update---------')
        update_contact()
        print('------------------------')
    elif user_input == "Leave":
        break
    else:
        print('Invalid Input')
