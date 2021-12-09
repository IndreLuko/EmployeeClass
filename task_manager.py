import utils
from task_class import Task
from datetime import date
import constant


class TaskManager:

    def __init__(self):
        self.task_list = self.__fill()

    @staticmethod
    def __fill():
        return [
            Task(1555, "File", "Archive old documents", 8, constant.STATUS_NEW, date(2021, 11, 20), "", ""),
            Task(1325, "Call", "Call a client", 10, constant.STATUS_NEW, date(2021, 11, 24), "", ""),
            Task(1101, "Post", "Post today's mail", 7, constant.STATUS_IN_PROGRESS, date(2021, 11, 24), "", 2587),
            Task(1132, "Report", "Create end of month reports", 10, constant.STATUS_COMPLETED, date(2021, 11, 21),
                 "2021-11-29", 1033)
        ]

    def list_tasks(self):
        for task in self.task_list:
            task.print()

    def new_task(self):
        new_task = Task(utils.id_randomizer(), Task.selection_task_name(), Task.selection_definition(),
                        Task.selection_priority(), constant.STATUS_NEW, date.today(), "", "TBD")
        self.task_list.append(new_task)
        new_task.print()

    def delete(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                index = self.task_list.index(task)
                self.task_list.pop(index)
                print(f"\nTask ID {task_id} has been deleted!")
                #TD (Technical Debt) - might be improved in future

    def get_id(self):
        while True:
            try:
                task_id = int(input("Please enter task ID: "))
                for task in self.task_list:
                    if task.task_id == task_id:
                        return task_id
                else:
                    print("Task ID you entered does not exist!")
            except ValueError:
                print("Value error! Please enter valid Task ID!")

    def assign_task(self, employee_id, task_id):
        if self.__task_already_assigned(employee_id):
            print("This employee already has a task assigned to them, please select another employee.")
        else:
            self.__assigned(employee_id, task_id)

    def complete_task(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                if task.status == constant.STATUS_NEW:
                    print("Error! This task has not been assigned and therefore cannot be completed.")
                elif task.status == constant.STATUS_COMPLETED:
                    print("Error! This task has already been completed.")
                else:
                    task.status = constant.STATUS_COMPLETED
                    task.completion_date = date.today()
                    print(f"Task {task.task_name} with ID {task.task_id} has been successfully completed")

    def completed_task_list(self):
        for task in self.task_list:
            if task.status == constant.STATUS_COMPLETED:
                task.print()

    def sorting(self):
        assigned = [(task.task_id, task.priority, task.creation_date, task.assigned_to)
                    for task in self.task_list if task.assigned_to == ""]
        unassigned_tasks_sorted = sorted(sorted(assigned, key=lambda x: x[2]), key=lambda x: x[1], reverse=True)
        return unassigned_tasks_sorted[0][0]

    def __task_already_assigned(self, employee_id):
        for task in self.task_list:
            if task.assigned_to == employee_id:
                return True

    def change_status(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                if task.status == constant.STATUS_NEW:
                    print("Task has not been assigned, so it cannot be failed.")
                elif task.status == constant.STATUS_COMPLETED:
                    print("Task has been completed, so it cannot be failed.")
                else:
                    task.status = constant.STATUS_NEW
                    print("Task status has been changed")

    def __assigned(self, employee_id, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                task.assigned_to = employee_id
                task.status = constant.STATUS_IN_PROGRESS
                print(f"Task {task.task_name} with ID {task.task_id} has been assigned to employee ID {employee_id}")
