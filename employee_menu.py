from employee_manager import EmployeeManager
from employee_class import Employee

print('What would you like to do:')
print('1. Hire new employee')
print('2. List employees')
print('3. Delete employee')
print('4. Terminate employee')
print('5. See all existing employees')
print("6. Change employee's phone number")
print('0 to quit')

selection = 1
employee_manager = EmployeeManager()
while selection != 0:
    selection = Employee.selection()
    if selection == 1:
        employee_manager.hire_employee(Employee.selection_name(), Employee.selection_surname(), Employee.selection_age(), Employee.selection_employment_date(), Employee.selection_day_of_leaving(), Employee.selection_phone_number())
    elif selection == 2:
        employee_manager.list()
    elif selection == 3:
        employee_manager.delete(Employee.selection_phone_number())
        employee_manager.list()
    elif selection == 4:
        employee_manager.terminate(Employee.selection_phone_number(), Employee.selection_actual_day_of_leaving())
        employee_manager.list()
    elif selection == 5:
        employee_manager.all_existing()
    elif selection == 6:
        employee_manager.change_phone(Employee.selection_phone_number(), Employee.selection_new_phone_number())