import datetime


class Employee:

    def __init__(self, name, surname, age, employment_date, day_of_leaving, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.employment_date = employment_date
        self.day_of_leaving = day_of_leaving
        self.phone_number = phone_number

    def print(self):
        print(
            f'Name:\t{self.name}\tSurname:\t{self.surname}\tAge:\t{self.age}'
            f'\tEmployment date:\t{self.employment_date}\t'
            f'Date of leaving:\t{self.day_of_leaving}\t\tPhone number:\t{self.phone_number}')

    @staticmethod
    def selection():
        while True:
            try:
                selection = int(input('Enter your choice here (1, 2, 3, 4, 5 or 6): '))
                if 0 <= int(selection) < 7:
                    return selection
                else:
                    print("Invalid format. Please enter number between 1 and 6")
            except ValueError:
                print("Invalid format. Please enter number between 1 and 6")

    @staticmethod
    def selection_name():
        while True:
            try:
                x = Employee._validate_name(str(input("Name: ")))
                if x:
                    return x
            except ValueError:
                print(f"Value error! Please enter valid name!")

    @staticmethod
    def selection_surname():
        while True:
            try:
                x = Employee._validate_name(str(input("Surname: ")))
                if x:
                    return x
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
                x = Employee._validate_date(int(input("Employment date. Year: ")), int(input("Month: ")),
                                            int(input("Day: ")))
                if x is not None:
                    if x <= datetime.date.today():
                        return x
            except ValueError:
                print("Invalid format! Date format must be YYYY MM DD")

    @staticmethod
    def selection_day_of_leaving():
        while True:
            try:
                day_of_leaving = input(str('Date of leaving or N/A: '))
                if day_of_leaving == 'N/A':
                    return day_of_leaving
                else:
                    x = Employee._validate_date(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
                    if x is not None:
                        return x
            except ValueError:
                print("Date of leaving format must be either YYYY MM DD or N/A")

    @staticmethod
    def selection_phone_number():
        while True:
            try:
                Employee._validate_text(1, 0)
                x = Employee._validate_phone(int(input()))
                if x:
                    return x
            except ValueError:
                print('Invalid format! Phone number must be 9 digits long in a format 86xxxxxxx')

    @staticmethod
    def selection_new_phone_number():
        try:
            Employee._validate_text(0, 1)
            x = Employee._validate_phone(int(input()))
            if x:
                return x
        except ValueError:
            print('Invalid format! Phone number must be 9 digits long in a format 86xxxxxxx')

    @staticmethod
    def selection_actual_day_of_leaving():
        while True:
            try:
                print("Enter actual date of leaving below")
                x = Employee._validate_date(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
                return x
            except ValueError:
                print("Incorrect format! Date format must be YYYY MM DD")

    @staticmethod
    def _validate_date(year, month, day):
        date = datetime.date(int(year), int(month), int(day))
        if len(str(year)) == 4:
            return date
        else:
            print("Year must be four digits, e.g. 2021")

    @staticmethod
    def _validate_phone(phone):
        if len(str(phone)) == 9:
            return phone
        else:
            print('Phone number must be 9 digits long in a format 86xxxxxxx')

    @staticmethod
    def _validate_text(current, new):
        if current == 1:
            print("Please enter current phone number below")
        if new == 1:
            print("Please enter new phone number")

    @staticmethod
    def _validate_name(name):
        if name.isalpha():
            return name
        else:
            print("Error! Only alphabetical characters allowed.")
