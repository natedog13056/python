from EmployeeModule import *
from SalaryModule import *

mary = Secretary('Mary', 'HR', '212-220-0987')
tom = Manager('Tom', 'IT', 'senior')
linda = Manager('Linda', 'Finance', 'junior')
jake = Director('Jake', 'Strategy', 'senior', mary, [tom, linda])

mary.about()
print('My salary is ' + str(getSalary(mary)))
tom.about()
print('My salary is ' + str(getSalary(tom)))
linda.about()
print('My salary is ' + str(getSalary(linda)))
jake.about()
print('My salary is ' + str(getSalary(jake)))