# Base class
class Company:
    def __init__(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

    def display_company_details(self):
        print("Company Name:", self.name)
        print("City:", self.city)
        print("Mobile No:", self.mobile_no)

# Derived class
class Employee(Company):
    def __init__(self, name, city, mobile_no, emp_name, designation, salary):
        # Initialize base class attributes
        super().__init__(name, city, mobile_no)
        # Initialize derived class attributes
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

    def display_employee_details(self):
        # Display company details
        self.display_company_details()
        # Display employee details
        print("Employee Name:", self.emp_name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

# Creating an object of Employee class
employee1 = Employee(
    name="Tech Solutions",
    city="New York",
    mobile_no="123-456-7890",
    emp_name="Alice Johnson",
    designation="Software Developer",
    salary=85000
)

# Displaying employee details
employee1.display_employee_details()
