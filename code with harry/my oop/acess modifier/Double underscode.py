""" Double underscode:-
    1)Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore)
    is textually replaced with _classname__spam, where classname is the current class name with leading
    underscore(s) stripped. 
    2)This mangling is done without regard to the syntactic position of the identifier,
    so it can be used to define class-private instance and class variables, methods, variables stored in globals,
    and even variables stored in instances. private to this class on instances of other classes. 
"""
class employee:
    def __init__(self):
        self.__name="harry"
""" I can not acess this op:- AttributeError: 'employee' object has no attribute '__name' """
a=employee()
# dont concentrate on self just look at .name
# print(a.__name)   # Can not be acess directly
print(a._employee__name)         # Can be acess indirectly
print(a.__dir__())      # name maangling to make class and sub class private

# another eg. -->

class Myclass:
    def __init__(self):
        self.__a="super privat word"
        self._semiprivate="semi private word"

mc=Myclass()
print(mc._semiprivate)
# print(mc.__superprivate)    # AttributeError: 'Myclass' object has no attribute '__superprivate'
print(mc._Myclass__a)         # it can be acess indirectly

