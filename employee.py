class Employee:
    no_of_leaves=9
    def printdetails(self):
        print(f"Name is {self.name} salary is {self.salary} and role is {self.role}")
    
Alish=Employee()
Kunal=Employee()

Alish.name="Alish"
Alish.salary=2000000
Alish.role="Programmer"

Kunal.name="Kunal"
Kunal.salary=51000
Kunal.role="Pilot"
print(Alish.printdetails())
