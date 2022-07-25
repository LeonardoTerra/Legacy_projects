import random
import string
import re


def password_validation():
    # Here we define a loop that will play until the user inputs an INT value.
    while True:
        # The TRY allows us to see whether the input is an INT or not. If it's not, the ValueError plays its role.
        try:
            password_length = int(input('How long should the password be: '))
            # Here is an IF to check whether the password is too long or too small. It gives the user an advice.
            if password_length >= 8:
                return password_length
            elif password_length < 8:
                return password_length
        except ValueError:
            print("Please, provide a number")


def manual_password_generator():
    # Here I built the regex that will serve as the condition
    password = []
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    while True:
        user_input = input('Choose a password: ')
        check = pattern.fullmatch(user_input)  # This check allows me to see whether the password matches the conditions
        if check is not None:
            print('All Right!')
            password.append(user_input)
            break
        else:
            requirements = {
                "1": 'Your Password should contain the following requirements:',
                "2": '8 Digits or more',
                "3": '1 Capital letter',
                "4": '1 Number',
                "5": '1 Symbol'
            }
            for v in requirements.values():
                print(v)
    return "".join(
        password)  # We use join like this in order to print something without brackets. It can be a print or a return.


def auto_password_generator():
    # Here is the list that will store the password and the var that will generate the letters and symbols that will be used.
    password = []
    characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

    # Here we loop throughout the values above in order to select them and print the password.
    for i in range(password_validation()):
        random_characters = random.choice(characters)
        password.append(random_characters)
        random.shuffle(password)  # Change the order of the values. Make it become unpredictable
    return "".join(
        password)  # We use join like this in order to print something without brackets. It can be a print or a return.

# def main():
# auto_password_generator()

# if __name__ == "__main__":
# main()

# READ.ME

# This code allows you to use one of the functions above to create a password.
# This code doesn't have an user GUI or a Web app yet. Feel free to improve it.
