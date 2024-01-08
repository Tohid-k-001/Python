class Employee:
    company="Apple"

    def show(self):
        """ Why I am not writing show(self,name,company) :-
        Here I can directly pass self.name and self.company by defining variable by object of class --> 14 """
        
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changecompany(self, newcompany):
        self.company=newcompany

e1=Employee()
e1.name="Harry"
e1.show()
e1.changecompany("Google")   # The class variable is not changing --> Its first argument is taking as an Instance variable 
                             # 1] To change use @Classmethod
e1.show()

# e2=Employee()
# e2.name="tohid"
# e2.show()
""" Instead of doing above just to know the company variable name changed or not """
print(Employee.company)
