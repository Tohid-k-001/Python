""" 
python doc string are the string literaks that appers right 
after the defination of function , method, class or module
 """

"""
# Using return concept (it will return the value where the function is called) 
def square (n):
    # Takes the number and return in square
    return (n*n)

num=square(6)
print(num) """

def square (n):
    # print(n)            #output:- 8
                        #         64
                        #         None

    """ 1.It should right above the function 
        2. Its not a string .
        3. It shoud in Triple cote.  
        4.Stores in atribute  """
    """ Takes the number and return in square """    
    # Its a Doc String not comment
    print(n*n)
square(8)
# print doc instruction
print(square.__doc__)   

#Pep 8
# if you write import this it will write a poem  "Zen of python" by Tim Peters
# its a ester egg in python 
""" 
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
 """
