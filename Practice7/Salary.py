from Practice7.Employee import *

def getSalary(employee):
    if isinstance(employee, Director):
        return 10000
    elif isinstance(employee, Manager):
        return 8000
    elif isinstance(employee, Secretary):
        return 5000