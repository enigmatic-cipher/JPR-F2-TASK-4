"""
Modify the class Employee in Task1. Add a constructor which takes name and salary as input and initializes them. It also computes the designation. If salary is greater than 40000 it is Manager other wise it is Developer. Also add a method printEmployee in the class. In another class create an object of the class Employee and print it.
"""

class Employee:
  def __init__(self,name,salary,designation):
    self.name = name
    self.salary = salary
    if (salary > 40000):
      self.designation = "Manager"
    else:
      self.designation = "Developer"

  def __str__(self):
    return "Employe Details: Name: {}, Salary: {}, & Designation: {}".format(self.name,self.salary,self.designation)

emp_1 = Employee("Rohit", 45000, "")
print(emp_1)
