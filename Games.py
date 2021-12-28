import random

win = 0
lose = 0

games = ('1: Dice Rolling', '2: Number Guessing')


# Games

def dice_rolling():
    print('------- Dice Game --------')
    print("Rolling the dice...")
    a = random.randint(1, 6)
    return a


def number_guessing():
    print('----- Number Guessing ----')
    print("Spinning the wheel...")
    a = random.randint(1, 100)
    return a


# Main code

print('--------- Games ---------')
for i in games:
    print(f'{i}')

while True:
    play_game = input('Do you want to game: ')
    if play_game == 'Yes' or play_game == 'yes':
        which_game = input('Which game: ')
        if which_game == str(1):
            game = dice_rolling()
            hint = int(input("Hint: "))
            if hint == game:
                print('Correct!')
                win += 1
            else:
                print('You lose!')
                lose += 1
        elif which_game == str(2):
            game = number_guessing()
            closest_bellow = game - 5
            closest_above = game + 5
            print(f'Number is close to {closest_bellow} and {closest_above}')
            hint = int(input("Hint: "))
            if hint == game:
                print('Correct!')
                win += 1
            else:
                print('You lose!')
                lose += 1
    elif play_game == "No" or play_game == "no":
        print("Ok. Hope to see you another time!")
        break
    else:
        print('invalid Option')

print("Lose:", lose)
print("Win:", win)
