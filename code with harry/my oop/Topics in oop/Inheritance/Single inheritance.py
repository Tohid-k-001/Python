class employee:
    no_of_leaves=8
    def __init__(self,name,salary,role) -> None:
        self.name=name
        self.salary=salary
        self.role=role

    def infoemp(self):
        print(f"the name of employee  is {self.name} and his salary is {self.salary} an profession is {self.role}")

    @classmethod
    def change_leaves(cls,nleave):
        cls.no_of_leaves= nleave

    @classmethod
    def fromstr(self,str):
        return self(str.split(" "))

    @staticmethod
    def greet(str):
        print("this is good" + str)

class programmer(employee):
    def __init__(self, name, salary, role, languages) -> None:
        super().__init__(name, salary, role)                          # --> Code reusability ie. converting all variables into self.
        self.languages=languages

    def infopro(self):
        print(f"the programmers name is {self.name} his salary is {self.salary} and his proffesion is {self.role} his languages are {self.languages}")
        
harry=employee("harry",45000,"student")
tohid=employee("tohid",56000,"teacher")

# harry.info()
# harry.change_leaves(78)
print(harry.no_of_leaves)     # --> leaves for harry

""" IMP:- object of childclass can run methods of both class though their no of arguments are different """

shubham=programmer("shubham",45000,"Programmer",["python"])
karan=programmer("karan",90000,"programmer",["python","cpp"])
print(karan.infopro())
