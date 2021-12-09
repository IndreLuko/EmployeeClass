import random


def id_randomizer():
    random_id = random.randint(1000, 10000)
    return random_id


def validate_alpha_chars(name):
    if name.isalpha():
        return name
    else:
        print("Error! Only alphabetical characters allowed.")


def validate_length(string, length):
    if len(str(string)) != length:
        print('Phone number must be 9 digits long in a format 86xxxxxxx')
    else:
        return string
