from datetime import datetime
from datetime import date
import random


class Employee:
    def __init__(self, employee_id, name, surname, age, employment_date, day_of_leaving, phone_number):
        self.employee_id = employee_id
        self.name = name
        self.surname = surname
        self.age = age
        self.employment_date = employment_date
        self.day_of_leaving = day_of_leaving
        self.phone_number = phone_number

    def print(self):
        print(
            f'\nEmployee ID: {self.employee_id}\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}'
            f'\nEmployment date: {self.employment_date}\n'
            f'Date of leaving: {self.day_of_leaving}\nPhone number: {self.phone_number}\n'
        )

    @staticmethod
    def selection():
        while True:
            try:
                selection = int(input('Enter your choice here (1, 2, 3, 4, 5 or 6): '))
                if 0 <= int(selection) < 16:
                    return selection
                else:
                    print("Invalid format. Please enter number between 1 and 6")
            except ValueError:
                print("Invalid format. Please enter number between 1 and 6")

    @staticmethod
    def selection_name():
        while True:
            try:
                name = Employee.validate_name(str(input("Name: ")))
                if name:
                    return name
            except ValueError:
                print(f"Value error! Please enter valid name!")

    @staticmethod
    def selection_surname():
        while True:
            try:
                surname = Employee.validate_name(str(input("Surname: ")))
                if surname:
                    return surname
            except ValueError:
                print(f"Value error! Please enter valid surname!")

    @staticmethod
    def selection_age():
        while True:
            try:
                age = int(input("Age: "))
                if 18 < int(age) < 100:
                    return age
                else:
                    print("Invalid format! Age must be max_number_index number between 18 and 100")
            except ValueError:
                print("Invalid format! Age must be max_number_index number between 18 and 100")

    @staticmethod
    def selection_employment_date():
        while True:
            try:
                employment_date = datetime.strptime(input("Employment start date in a format YYYY-MM-DD: ")
                                                    , '%Y-%m-%d').strftime('%Y-%m-%d')
                if employment_date is not None:
                    if employment_date <= date.today().strftime('%Y-%m-%d'):
                        return employment_date
                    else:
                        print("Error! Employment date cannot be in future")
            except ValueError:
                print("Invalid format! Date format must be YYYY-MM-DD")

    @staticmethod
    def selection_day_of_leaving():
        while True:
            try:
                day_of_leaving = input(str('Date of leaving in a format YYYY-MM-DD or N/A: '))
                if not day_of_leaving:
                    return "N/A"
                if day_of_leaving == "N/A":
                    return day_of_leaving
                if day_of_leaving == datetime.strptime(day_of_leaving, '%Y-%m-%d').strftime('%Y-%m-%d'):
                    return day_of_leaving
            except ValueError:
                print("Date of leaving format must be either YYYY-MM-DD or N/A")

    @staticmethod
    def selection_phone_number():
        while True:
            try:
                Employee.validate_text(1)
                phone = int(input(""))
                if Employee.validate_phone(phone):
                    return phone
            except ValueError:
                print('Invalid format! Phone number must be 9 digits long in a format 86xxxxxxx')

    @staticmethod
    def selection_new_phone_number():
        try:
            Employee.validate_text(0)
            phone = int(input(""))
            if Employee.validate_phone(phone):
                return phone
        except ValueError:
            print('Invalid format! Phone number must be 9 digits long in a format 86xxxxxxx')

    @staticmethod
    def selection_actual_day_of_leaving():
        while True:
            try:
                day_of_leaving = datetime.strptime(input("Enter actual date of leaving: "),
                                                   '%Y-%m-%d').strftime('%Y-%m-%d')
                return day_of_leaving
            except ValueError:
                print("Incorrect format! Date format must be YYYY MM DD")

    @staticmethod
    def validate_phone(phone):
        if len(str(phone)) != 9:
            print('Phone number must be 9 digits long in max_number_index format 86xxxxxxx')
        else:
            return phone

    @staticmethod
    def validate_text(text):
        if text == 1:
            print("Please enter current phone number below")
        if text == 0:
            print("Please enter new phone number")

    @staticmethod
    def validate_name(name):
        if name.isalpha():
            return name
        else:
            print("Error! Only alphabetical characters allowed.")

    @staticmethod
    def id_randomizer():
        random_id = random.randint(1000, 10000)
        return random_id
