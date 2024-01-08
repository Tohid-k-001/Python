# 1) importing math and calling functions of math module by math. 
import math
print(math.floor(6.09473))
print(math.sqrt(9))      #output :- 3

# 2) Importing useful things only , so no need to write math. to use it
from math import sqrt,pi
square=sqrt(9) * pi                
print(square)

# 3) from math import *        # we are importing everything in our script (*)
"""  This will cause confusion when like pi is constant available in different system also so better 
    to import only to use things that you like to use """

# 4) As keyword :- To make shortcut of modules and functions

from math import pi,sqrt as sq
square=sq(9) * pi    #<--             
print(square)

import math as m
ans=m.sqrt(16)
print(ans)
""" Here we are importing the separate functions of math 
    in previous we imported the whole math so we have to call personally each function.  """

# 5) The dir function()
"""  It will show how many function does it have  in terminal!! """
import math
print(dir(math))     
print(math.nan,type(math.nan))


