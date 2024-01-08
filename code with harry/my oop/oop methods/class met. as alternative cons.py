class employee:
    def __init__(self,name,salary) -> None:
        self.name=name
        self.salary=salary

    #-->
    @classmethod
    def fromstring(self,string):
        return self(string.split("-")[0], string.split("-")[1])

e1=employee("harry",45000)
print(e1.name)
print(e1.salary)

string="harry-12000"

""" imp lesson from previous chap :-
    we are splitting the 'string' converting it into a list and accesing elements from string directly
    1.word = string.split("-")
    2.print(word[0])
    
    --> print(string.split("-")[0])  """

# e2=employee(string.split("-")[0],string.split("-")[1])
""" It looks to confusing for new coder if my data is comming in string so,
    --> def __init__(self, string.split("-")[0], string.split("-")[1]) 
    It will give me error   """

e2=employee.fromstring(string)
print(e2.name,e2.salary)
# Sol. is Alternative constructor --> make function to change data from string to list element 

# another eg.

class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    @classmethod
    def fromstr(self,str):
        # 1)
        name,age=str.split(" ")
        return self(name, int(age))
        # 2)
        return self(str.split(" ")[0],int(str.split(" ")[1]))

str="Tohid 56"
p=person.fromstr(str)
print(p.name, p.age)
