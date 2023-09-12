class Employee:
    salary = 89
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

rohan = Employee("rohan", "3500")
print(rohan.salary)
print(rohan.name)

nitin = Employee("nitin", "4500")
print(nitin.salary)
print(nitin.name)
