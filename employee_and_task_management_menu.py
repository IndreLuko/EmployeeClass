from employee_manager import EmployeeManager
from employee_class import Employee
from task_manager import TaskManager
from task_class import Task

print('What would you like to do:')
print('1. Hire new employee')
print('2. List employees')
print('3. Delete an employee')
print('4. Terminate an employee')
print('5. See all existing employees')
print("6. Change employee's phone number")
print("7. List all tasks")
print("8. Create new task")
print("9. Delete a task")
print("10. Assign new task")
print("11. Complete a task")
print("12. List all completed tasks")
print("13. Change task status")
print('0 to quit')

selection = 1
employee_manager = EmployeeManager()
task_manager = TaskManager()
while selection != 0:
    selection = Employee.selection()
    if selection == 1:
        employee_manager.hire_employee(
            Employee.selection_name(), Employee.selection_surname(), Employee.selection_age(),
            Employee.selection_employment_date(), Employee.selection_day_of_leaving(), Employee.selection_phone_number()
        )
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
    elif selection == 7:
        print("")
        task_manager.list_tasks()
    elif selection == 8:
        task_manager.new_task(Task.selection_task_name(), Task.selection_definition(), Task.selection_priority())
    elif selection == 9:
        task_manager.delete(task_manager.get_id())
        task_manager.list_tasks()
    elif selection == 10:
        task_manager.assign_task(employee_manager.get_id(), task_manager.sorting())
    elif selection == 11:
        task_manager.complete_task(task_manager.get_id())
    elif selection == 12:
        task_manager.completed_task_list()
    elif selection == 13:
        task_manager.change_status(task_manager.get_id())
