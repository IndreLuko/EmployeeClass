from employee_class import Employee
import utils


class EmployeeManager:

    def __init__(self):
        self.employee_list = self.fill()

    def list(self):
        for employee in self.employee_list:
            employee.print()

    def hire_employee(self):
        new_hire = Employee(utils.id_randomizer(), Employee.selection_name(), Employee.selection_surname(),
                            Employee.selection_age(), Employee.selection_employment_date(),
                            Employee.selection_day_of_leaving(), Employee.selection_phone_number())
        self.employee_list.append(new_hire)
        new_hire.print()

    @staticmethod
    def fill():
        return [
            Employee(1050, 'Liutauras', 'Pamuk', 37, '2017-12-10', '2021-01-10', 867821469),
            Employee(1189, 'Reda', 'Krasauske', 55, '2013-07-11', 'N/A', 864571584),
            Employee(8754, 'Raminta', 'Bugeliene', 45, '2015-08-25', '2020-11-15', 861188574),
            Employee(5794, 'Vilius', 'Ragauskas', 29, '2018-10-08', 'N/A', 868965571),
            Employee(2587, 'Rugile', 'Taranovic', 40, '2012-03-15', '2015-04-15', 867418529),
            Employee(6974, 'Romas', 'Kalvinskas', 27, '2019-02-21', 'N/A', 867514873),
            Employee(1033, 'Renata', 'Starinske', 31, '2014-05-04', 'N/A', 869521467),
            Employee(9987, 'Raigardas', 'Vernt', 44, '2016-06-12', '2019-05-22', 865716998)
        ]

    def delete(self, employee_id):
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                index = self.employee_list.index(employee)
                self.employee_list.pop(index)
                print(f"\nEmployee ID {employee_id} has been deleted!\n")
                return employee_id
                # TD (Technical Debt) - might be improved in future

    def terminate(self, employee_id):
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                employee.day_of_leaving = Employee.selection_actual_day_of_leaving()
                employee.print()

    def all_existing(self):
        print("All Active employees:")
        for employee in self.employee_list:
            if employee.day_of_leaving == 'N/A':
                employee.print()

    def change_phone(self):
        phone = Employee.selection_phone_number()
        new_phone = Employee.selection_new_phone_number()
        for employee in self.employee_list:
            if employee.phone_number == phone:
                employee.phone_number = new_phone
                employee.print()

    def get_id(self):
        while True:
            try:
                employee_id = int(input("Please enter employee ID: "))
                for employee in self.employee_list:
                    if employee.employee_id == employee_id:
                        return employee_id
                else:
                    print("Employee ID you entered does not exist!")
            except ValueError:
                print("Value error! Please enter valid Employee ID!")

    def list_employee(self, employee_id):
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                employee.print()
