from task_class import Task
from datetime import date


class TaskManager:

    def __init__(self):
        self.task_list = self.fill()

    @staticmethod
    def fill():
        return [
            Task(555, "File", "Archive old documents", 8, "new", date(2021, 11, 20), "", ""),
            Task(325, "Call", "Call a client", 10, "new", date(2021, 11, 24), "", ""),
            Task(101, "Post", "Post today's mail", 7, "in progress", date(2021, 11, 24), "", 2587),
            Task(132, "Report", "Create end of month reports", 10, "completed", date(2021, 11, 21), "2021-11-29", 1033)
        ]

    def list_tasks(self):
        for task in self.task_list:
            task.print()

    def new_task(self, task_name, definition, priority):
        new_task = Task(Task.id_randomizer(), task_name, definition, priority, "new", date.today(), "", "TBD")
        self.task_list.append(new_task)
        new_task.print()

    def delete(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                ind = self.task_list.index(task)
                self.task_list.pop(ind)
                print(f"\nTask {task_id} has been deleted!\n")

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
        if self.task_already_assigned(employee_id) == 1:
            print("This employee already has a task assigned to them, please select another employee.")
        else:
            self.assigned(employee_id, task_id)

    def complete_task(self, task_id):
        for i in self.task_list:
            if i.task_id == task_id:
                if i.status == "new":
                    print("Error! This task has not been assigned and therefore cannot be completed.")
                elif i.status == "completed":
                    print("Error! This task has already been completed.")
                else:
                    i.status = "completed"
                    i.completion_date = date.today()
                    print("")
                    print(f'Task ID {task_id} has been successfully completed!\n')
                    i.print()

    def completed_task_list(self):
        for task in self.task_list:
            if task.status == "completed":
                task.print()

    def sorting(self):
        assigned = [(task.task_id, task.priority, task.creation_date, task.assigned_to)
                    for task in self.task_list if task.assigned_to == ""]
        unassigned_tasks_sorted = sorted(sorted(assigned, key=lambda x: x[2]), key=lambda x: x[1], reverse=True)
        return unassigned_tasks_sorted[0][0]

    def task_already_assigned(self, employee_id):
        for task in self.task_list:
            if task.assigned_to == employee_id:
                return 1

    def change_status(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                if task.status == "new":
                    print("Task has not been assigned, so it cannot be failed.")
                elif task.status == "completed":
                    print("Task has been completed, so it cannot be failed.")
                else:
                    task.status = "new"
                    print("Task status has been changed")

    def assigned(self, employee_id, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                task.assigned_to = employee_id
                task.status = "in progress"
                print(f"Task {task.task_name} with ID {task.task_id} has been assigned to employee ID {employee_id}")
