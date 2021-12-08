from employee_class import Employee


class EmployeeManager:

    def __init__(self):
        self.employee_list = self.fill()

    def list(self):
        for emp in self.employee_list:
            emp.print()

    def hire_employee(self, name, surname, age, employment_date, day_of_leaving, phone_number):
        new_hire = Employee(name, surname, age, employment_date, day_of_leaving, phone_number)
        self.employee_list.append(new_hire)
        new_hire.print()

    @staticmethod
    def fill():
        return [Employee('Liutauras', 'Pamuk', 37, '2017-12-10', '2021-01-10', 867821469),
                Employee('Reda', 'Krasauske', 55, '2013-07-11', 'N/A', 864571584),
                Employee('Raminta', 'Bugeliene', 45, '2015-08-25', '2020-11-15', 861188574),
                Employee('Vilius', 'Ragauskas', 29, '2018-10-08', 'N/A', 868965571),
                Employee('Rugile', 'Taranovic', 40, '2012-03-15', '2015-04-15', 867418529),
                Employee('Romas', 'Kalvinskas', 27, '2019-02-21', 'N/A', 867514873),
                Employee('Renata', 'Starinske', 31, '2014-05-04', 'N/A', 869521467),
                Employee('Raigardas', 'Vernt', 44, '2016-06-12', '2019-05-22', 865716998)]

    def delete(self, phone_number):
        ind = 0
        for i in self.employee_list:
            if i.phone_number == phone_number:
                self.employee_list.pop(ind)
            ind += 1

    def terminate(self, phone_number, new_day_of_leaving):
        for i in self.employee_list:
            if i.phone_number == phone_number:
                i.day_of_leaving = new_day_of_leaving

    def all_existing(self):
        print("All Active employees:")
        for i in self.employee_list:
            if i.day_of_leaving == 'N/A':
                i.print()

    def change_phone(self, phone_number, new_number):
        for i in self.employee_list:
            if i.phone_number == phone_number:
                i.phone_number = new_number
                i.print()
