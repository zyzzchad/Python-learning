class Employee:
    no_of_leaves=9
    def __init__(self,name,salary,role):
        self.name= name
        self.salary=salary
        self.role=role
    
    def printdetails(self):
        return(f"The name is{self.name},classs is {self.classs},and the role is {self.role}")

alish= Employee("Alish",2000000,"Programmer")
print(alish.salary)
    