# Main idiom functions

def pt_converter():
    cm = input("Qual a sua altura em metros: ")
    total = round(float(cm) * 3.281, 2)
    print(f'Sua altura é de {total} pés')


def en_converter():
    cm = input('how tall are you in meters? ')
    total = round(float(cm) * 3.281, 2)
    print(f' Your height is {total} feet')


# Conditional statement

question = input('Language: ')

if question == "Pt" or question == "pt":
    print(pt_converter())
elif question == 'En' or question == "en":
    print(en_converter())
else:
    print('Invalid answer')
