""" 
if we want to change the 6th element of the file then 
1.we read the file 
2. we change the 6th element of the file 
3.then we again write the file
this is not the efficient way to do!
 """

""" In python the seek() and tell() function are used to work with file objects and their position within the file.
    Those function are the part of built in io module which provides a consistent interface for reading and writing 
    to various file like objects, such as files, pipes and in- memory buffers.  """

""" 1)The seek() function allows you to move the current position to a specific function within a file.
    2)The position is specified by bytes and you can move forward or backward from the current position. """



with open('tohid_file3.txt','r') as f:
    print(type(f))  
    # output:- <class '_io.TextIOWrapper'>
    f.seek(8)       # It seeks the content of given bytes from start
        
    data=f.read(5)  # it read given bytes
    print(data)


