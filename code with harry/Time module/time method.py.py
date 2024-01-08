import time
""" time.sleep() :- Code will stop working for given sec. """
print(6)
time.sleep(3)
print("I am printed after 3 sec.")

print(time.strftime("Year=%y Month=%m Date=%D %H:%M:%S"))
# op:- Year=23 Month=12 Date=12/29/23 16:43:18


""" If you are not in local time then for that case:-- """
t=time.localtime()
print(t)
# op:- time.struct_time(tm_year=2023, tm_mon=12, tm_mday=29, tm_hour=16, tm_min=33, tm_sec=14, tm_wday=4, tm_yday=363, tm_isdst=0)
formated_time=time.strftime("%D %H:%M:%S",t)
print(formated_time)
# op:- 12/29/23 16:46:48 

