class My_class:
    def __init__(self,value):
        self._value=value               # the _ is necessary (AttributeError: property 'value' of 'My_class' object has no setter)
                                        # this is _value is setter (coz. self. is always)

    def show(self):
        print(f"The value is {self._value}")

    @property                           # this is the way to set getter 
    def Ten_value(self):                # This becomes a getter
        return 10*self._value
    
    @Ten_value.setter                    
    def Ten_value(self,newvalue):        
        self._value=newvalue/10
    
obj=My_class(100)         # 1) Create object of class first
                        # 2) Pass the argument value for class 89=value --> value=self._value
                        # The function inside the class is called
obj.Ten_value = 67      # This is not a method to set a value
""" This is giving parameter to the given function , so we have to add a new parameter to the function  """

""" IMP :- All functions inside the class contain self default parameter """

print(obj.Ten_value)      
""" After passing the value the Ten_value is set by classes 
    If you want to set the value then use setter"""
obj.show()

