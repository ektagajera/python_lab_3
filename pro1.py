class Employee:
    def __init__(self, name, date_of_joining, designation, salary):
        self.name = name
        self.date_of_joining = date_of_joining
        self.designation = designation
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Date of Joining:", self.date_of_joining)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

# Creating an object of Employee class
employee1 = Employee(
    name="John Doe",
    date_of_joining="2024-08-01",
    designation="Software Engineer",
    salary=70000
)

# Displaying the employee details
employee1.display_details()
                                                        