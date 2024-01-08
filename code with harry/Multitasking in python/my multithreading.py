import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Some function is executing
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return 
def main():
    # python is specially built in such a way that it executes each instruction one by one 
    time1=time.perf_counter()
    # running code one by one
    # func(4)
    # func(3)
    # func(2)

    # Same code using thread:-
    t1=threading.Thread(target=func,args=[4])
    t2=threading.Thread(target=func,args=[3])
    t3=threading.Thread(target=func,args=[1])
    t1.start()
    t2.start()
    t3.start()

    # op:- Time required to run the function: 0.0020818000193685293
    # it through's the function to run and return after completion in background so it gives 0 sec. but the program ends after 4sec.
    # --> If I want to stop until it completes, then 

    """ It starts on above statement we just wait to complete everything """
    t1.join()   #--> if I stop then it stops for 4 sec.
    t2.join()   #--> it stops for 3 sec.
    t3.join()   #--> it stops for 1 sec.
                #--> when I run above all then it wait for 4 sec. in that 4 sec. all other functions had run

    time2=time.perf_counter()
    print("\nTime required to run the function:",time2-time1)

# main()

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        time1=time.perf_counter()
        future1 = executor.submit(func,4)
        future2 = executor.submit(func,3)
        future3 = executor.submit(func,4)
        print(future1.result())  
        print(future2.result())
        print(future3.result())
        
        """ conclusion:-
            1)here all runs at same time after completion the task it returns the value one by one  
            2)After 4 sec. it returns all values """

        # 3.Syntax:- If there are 500 url's then we dont do like url1, url2 ... we use a list and operate it
        # l=[1,3,1,3,4,3,2]
        # results=executor.map(func,l)
        # for result in results:
        #     print(result)
        # to calculate time
        time2=time.perf_counter()
        print("time taken to complete the task: ",time2-time1)

        """ conclusion:-
            1)all process runs in the background parallel 
            2)Return the values after execution whose complete first displays first but the time is the biggest time required
            3) op:- 4.0041"""
poolingDemo()

print("the instruction executes after returning the all values")





