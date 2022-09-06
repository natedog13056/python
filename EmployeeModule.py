# Employee Module

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class Secretary(Employee):
    def __init__(self, name, department, telephone):
        super().__init__(name, department)

        self.telephone = telephone

    def about(self):
        print('My name is ' + self.name + ', I am working as a secretary in department ' + self.department + '. My telephone is ' + self.telephone)

class Manager(Employee):
    def __init__(self, name, department, level):
        super().__init__(name, department)

        self.level = level

    def about(self):
        print('My name is %s, I am working as a %s manager in department %s' % (self.name, self.level, self.department))

class Director(Manager):
    def __init__(self, name, department, level, assistant, directReport):
        super().__init__(name, department, level)

        self.assistant = assistant # Secretary object
        self.directReport = directReport #[Manager object 1, Manager object 2]

    def about(self):
        super().about()
        print('I am promoted to Director now. My secretary is ' + self.assistant.name + '. I have total ' + str(len(self.directReport)) + ' direct reporter.')