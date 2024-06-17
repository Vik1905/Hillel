class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department):
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language):
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    pass

