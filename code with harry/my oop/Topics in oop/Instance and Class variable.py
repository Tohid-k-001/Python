class employee:
    company_name="apple"                  # Class variable --> Use it by self. in class 
#                                                           If instance variable is not present then it will find class variable to change
    def __init__(self,name):     # Constructor
        self.name=name
        self.raise_amount=0.02           # Instant variable --> That I can change first              
        # self.company_name="Google"
    
    def show_details(self):
        print(f"the name of employee is : {self.name}  and the company name is : {self.company_name} raise amount is : {self.raise_amount}")

""" Why we use Self argument in every function :-
    Here both are giving the same output when I remove the self from [def show_details()] then it gives error
    ie. TypeError: employee.show_details() takes 0 positional arguments but 1 was given """
# emp1.show_details()

# employee.show_details(emp1)    --> one variable is by default passing so you have to write self inside the function

emp1=employee("harry")
emp1.raise_amount = 0.3    # I am changing the instant value for 1 employee
emp1.company_name="Apple India"
emp1.show_details()
emp2=employee("Tohid")
emp2.show_details()
print(emp2.company_name)

