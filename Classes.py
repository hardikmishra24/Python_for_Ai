class Employee:

    # self -> Refers to the CURRENT OBJECT being created (similar to 'this' in C#).
    # Python automatically passes the object as the first argument.
    
      
  
    
    # inside this constructor:
    # self   = emp1
    # name   = "Mohan"
    # salary = 80000
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
      return self.salary * 0.10

emp1 = Employee("Mohan", 80000)
emp1.name
emp1.salary 
emp1.calculate_bonus()   