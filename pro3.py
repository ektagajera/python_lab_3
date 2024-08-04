# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Base class 2
class Employee:
    def __init__(self, employee_id, designation):
        self.employee_id = employee_id
        self.designation = designation

    def display_employment_details(self):
        print("Employee ID:", self.employee_id)
        print("Designation:", self.designation)

# Derived class using multiple inheritance
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, designation, department):
        # Initialize Person and Employee using super()
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, designation)
        self.department = department

    def display_manager_details(self):
        # Display personal details
        self.display_personal_details()
        # Display employment details
        self.display_employment_details()
        # Display department
        print("Department:", self.department)

# Creating an object of Manager class
manager1 = Manager(
    name="John Smith",
    age=40,
    employee_id="E12345",
    designation="Senior Manager",
    department="Sales"
)

# Displaying manager details
manager1.display_manager_details()
