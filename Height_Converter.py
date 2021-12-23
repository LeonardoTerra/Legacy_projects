# Main conversor functions

def pt_feet_converter():  # Portuguese foot converter
    cm = input("Qual a sua altura em metros: ")
    total = round(float(cm) * 3.28084, 2)
    print(f'Sua altura é de {total} pés')


def pt_meters_converter():  # Portuguese meters converter
    feet = input('Qual a sua altura em pés? ')
    total = round(float(feet) * 0.3048, 2)
    print(f'Sua altura é de {total} metros')


def en_feet_converter():  # English foot converter
    cm = input('How tall are you in meters? ')
    total = round(float(cm) * 3.28084, 2)
    print(f'Your height is {total} feet')


def en_meters_converter():  # English meters converter
    feet = input('How tall are you in feet? ')
    total = round(float(feet) * 0.3048, 2)
    print(f'Your height is {total} Meters')


# Conditional statement

language = input('Language: ')

if language == "Pt" or language == "pt":
    conversor = input('Você quer converter metros ou pés? ')
    if conversor == 'metros':
        print(pt_meters_converter())
    elif conversor == 'pés' or conversor == 'pes':
        print(pt_feet_converter())
    else:
        print('Resposta ínvalida')

elif language == 'En' or language == "en":
    converter = input('Do you want to convert meters or foot? ')
    if converter == 'meters':
        print(en_meters_converter())
    elif converter == "foot":
        print(en_feet_converter())
    else:
        print("Invalid Answer")
else:
    print('Invalid Answer')
