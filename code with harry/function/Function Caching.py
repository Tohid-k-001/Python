""" Own words:- 
     when certain function takes so much time to generate some result if we have lot of functions to execute then its a problem 
     our lots of time is used , so the function caching is used here if a certain function is repeating in some manuals then it 
     remembers the result and when the function come it directly put the value of that function. """
# Here one module does it automatically:- 
# functools
import time

# import functools
# @functools.lru_cache(maxsize=None)
# --> 
from functools import lru_cache
@lru_cache(maxsize=None)

def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
# Explanation of run:-
# now it doesn't take a single second to run the below Program
# because it memoise from the cache

""" Memoisation :-
    Memoization is a technique used in computer science to speed up the execution of recursive or computationally
    expensive functions by caching the results of function calls and returning the cached results when the same 
    inputs occur again """ 
# imp:-
# 1)If I run the program again then it again take time 
# 2)the memory get deleted after from start
# 3)the cache takes memory it doesn't make any folder ie.it doesn't take any storage
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")









