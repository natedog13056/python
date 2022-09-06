class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class Secretary(Employee):
    def __init__(self, name, department, telephone):
        super().__init__(name, department)

        self.telephone = telephone

    def about(self):
        print('My name is %s, I am working as a secretary in department %s. My telephone is %s' % (self.name, self.department, self.telephone))

class Manager(Employee):
    def __init__(self, name, department, level):
        super().__init__(name, department)

        self.level = level

    def about(self):
        print('My name is %s, I am working as a %s manager in department %s.' % (
        self.name, self.level, self.department))

class Director(Manager):
    def __init__(self, name, department, level, assistant, directReport):
        super().__init__(name, department, level)

        self.assistant = assistant
        self.directReport = directReport

    def about(self):
        super().about()
        print('I am promoted to Director now. My secretary is %s. I have total %d direct reporters.' % (
            self.assistant.name, len(self.directReport)))