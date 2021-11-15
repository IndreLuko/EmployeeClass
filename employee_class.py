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
            f'Name: {self.name}| Surname: {self.surname}| Age: {self.age}| Employment date: {self.employment_date}|'
            f'Date of leaving: {self.day_of_leaving}| Phone number: {self.phone_number}')

    @staticmethod
    def selection():
        selection = input('Enter your choice here (1, 2, 3, 4, 5 or 6): ')
        if not selection:
            print("Selection cannot be blank")
        elif selection.isdigit() and 0 <= int(selection) < 7:
            return int(selection)
        else:
            print("Please enter number between 1 and 6")

    @staticmethod
    def selection_name():
        while True:
            name = str(input("Name: "))
            if not name:
                print("Name cannot be blank")
                continue
            elif name.isalpha():
                return name
            else:
                print("Name cannot contain numbers")

    @staticmethod
    def selection_surname():
        while True:
            surname = input("Surname: ")
            if not surname:
                print("Surname cannot be blank")
                continue
            elif surname.isalpha():
                return surname
            else:
                print("Surname cannot contain numbers")

    @staticmethod
    def selection_age():
        while True:
            age = input("Age: ")
            if not age:
                print("Age cannot be blank")
                continue
            elif age.isdigit() and 18 < int(age) < 100:
                return age
            else:
                print("Age must be a number between 18 and 100")

    @staticmethod
    def selection_employment_date():
        while True:
            employment_date = input('Employment date YYYY MM DD: ')
            if not employment_date:
                print("Employment date cannot be blank")
            elif not employment_date.isalpha():
                return employment_date
            else:
                print("Employment date must be a number")

    @staticmethod
    def selection_day_of_leaving():
        while True:
            day_of_leaving = input('Date of leaving (enter N/A if does not apply) YYYY MM DD: ')
            if not day_of_leaving:
                print("Date of leaving cannot be blank - enter N/A if it does not apply")
            elif day_of_leaving == 'N/A' or not day_of_leaving.isalpha():
                return day_of_leaving
            else:
                print("Date of leaving must be a number or N/A if it does not apply")

    @staticmethod
    def selection_phone_number():
        while True:
            phone_number = input('Phone number 86xxxxxxx: ')
            if not phone_number:
                print("Phone number cannot be blank")
                continue
            elif phone_number.isdigit() and len(phone_number) == 9:
                return phone_number
            else:
                print('Invalid format! Phone number must be 9 digits long in a format 86xxxxxxx')

    @staticmethod
    def selection_new_phone_number():
        while True:
            phone_number = input('New phone number 86xxxxxxx: ')
            if not phone_number:
                print("Phone number cannot be blank")
                continue
            elif phone_number.isdigit() and len(phone_number) == 9:
                return phone_number
            else:
                print('Invalid format! Phone number must be 9 digits long in a format 86xxxxxxx')

    @staticmethod
    def selection_actual_day_of_leaving():
        while True:
            actual_day_of_leaving = input('Date of leaving in a format YYYY MM DD: ')
            if not actual_day_of_leaving:
                print("Date of leaving cannot be blank")
                continue
            elif not actual_day_of_leaving.isalpha():
                return actual_day_of_leaving
            else:
                print("Date of leaving cannot contain letters")
