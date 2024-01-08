class math:
    def __init__(self,num):
        self._num=num

    def convert(self):
        self._num= 10*self._num
    
    @property
    def show(self):
        print(f"the double value is: {self._num}")
obj=math(2)
print(obj._num)
obj.convert()
obj.show()