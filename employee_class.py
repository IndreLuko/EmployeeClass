from datetime import datetime
from datetime import date
import utils
import constant


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
                if 0 <= int(selection) <= 13:
                    return selection
                else:
                    print("Invalid format. Please enter number between 1 and 6")
            except ValueError:
                print("Invalid format. Please enter number between 1 and 6")

    @staticmethod
    def selection_name():
        while True:
            try:
                name = utils.validate_alpha_chars(str(input("Name: ")))
                if name:
                    return name
            except ValueError:
                print(f"Value error! Please enter valid name!")

    @staticmethod
    def selection_surname():
        while True:
            try:
                surname = utils.validate_alpha_chars(str(input("Surname: ")))
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
                    print("Invalid format! Age must be a number between 18 and 100")
            except ValueError:
                print("Invalid format! Age must be a number between 18 and 100")

    @staticmethod
    def selection_employment_date():
        while True:
            try:
                employment_date = datetime.strptime(input("Employment start date in a format YYYY-MM-DD: ")
                                                    , constant.DATE_FORMAT).strftime(constant.DATE_FORMAT)
                if employment_date:
                    if employment_date <= date.today().strftime(constant.DATE_FORMAT):
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
                if day_of_leaving == datetime.strptime(day_of_leaving,
                                                       constant.DATE_FORMAT).strftime(constant.DATE_FORMAT):
                    return day_of_leaving
            except ValueError:
                print("Date of leaving format must be either YYYY-MM-DD or N/A")

    @staticmethod
    def selection_phone_number():
        while True:
            try:
                phone = Employee.__validate_phone(1)
                if phone:
                    return phone
            except ValueError:
                print('Invalid format! Phone number must be 9 digits long in a format 86xxxxxxx')

    @staticmethod
    def selection_new_phone_number():
        while True:
            try:
                phone = Employee.__validate_phone(0)
                if phone:
                    return phone
            except ValueError:
                print('Invalid format! Phone number must be 9 digits long in a format 86xxxxxxx')

    @staticmethod
    def selection_actual_day_of_leaving():
        while True:
            try:
                day_of_leaving = datetime.strptime(input("Enter actual date of leaving: "),
                                                   constant.DATE_FORMAT).strftime(constant.DATE_FORMAT)
                return day_of_leaving
            except ValueError:
                print("Incorrect format! Date format must be YYYY MM DD")

    @staticmethod
    def __validate_phone(text):
        if text == 1:
            phone = int(input("Please enter current phone number: "))
            if utils.validate_length(phone, 9):
                return phone
        if text == 0:
            phone = int(input("Please enter new phone number: "))
            if utils.validate_length(phone, 9):
                return phone



