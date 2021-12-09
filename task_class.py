import random


class Task:
    def __init__(self, task_id, task_name, definition, priority, status, creation_date, completion_date, assigned_to):
        self.task_id = task_id
        self.task_name = task_name
        self.definition = definition
        self.priority = priority
        self.status = status
        self.creation_date = creation_date
        self.completion_date = completion_date
        self.assigned_to = assigned_to

    def print(self):
        print(
            f'Task ID: {self.task_id}\nTask name: {self.task_name}\nDescription: {self.definition}\n'
            f'Priority: {self.priority}\nStatus: {self.status}\nCreation date: {self.creation_date}\n'
            f'Completion date: {self.completion_date}\nAssigned to: {self.assigned_to}\n'
        )

    @staticmethod
    def selection_task_name():
        while True:
            try:
                name = Task.validate_task_name(str(input("Task name: ")))
                if name:
                    return name
            except ValueError:
                print(f"Value error! Please enter valid name!")

    @staticmethod
    def selection_definition():
        while True:
            try:
                definition = str(input("Definition: "))
                if definition:
                    return definition
                else:
                    print("Definition cannot be blank")
            except ValueError:
                print(f"Value error! Please enter valid definition!")

    @staticmethod
    def selection_priority():
        while True:
            try:
                priority = int((input("Priority: ")))
                if 1 <= priority <= 10:
                    return priority
                else:
                    print("Please enter number between 1 and 10")
            except ValueError:
                print(f"Value error! Please enter valid priority number!")

    @staticmethod
    def id_randomizer():
        random_id = random.randint(100, 1000)
        return random_id

    @staticmethod
    def validate_task_name(task_name):
        if task_name.isalpha():
            return task_name
        else:
            print("Error! Name cannot be blank and only alphabetical characters allowed.")



