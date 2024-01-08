""" 1)The tell() function returns the current position of pointer within the file in bytes.
    2)This is useful for keeping track of location.
    3)Seeking to the a specific location relative to a current location """

with open('tohid_file3.txt','r') as f:
    print(type(f))  
    f.seek(6)
    """ If I want to know from where reading is started """
    
    print(f.tell()) # op:- 10    
    data=f.read(5)  # it read given bytes
    print(data)