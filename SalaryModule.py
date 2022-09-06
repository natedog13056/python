from EmployeeModule import *

def getSalary(obj):
    if isinstance(obj, Director):
        return 10000
    elif isinstance(obj, Manager):
        return 8000
    elif isinstance(obj, Secretary):
        return 5000