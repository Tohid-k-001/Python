f=open('tohid_file2.txt','w')

""" Writing files by making list which we want to print in file """
lines=["line1\n","line2\n","line3\n"]

# print(lines)        output:- ['line1\n', 'line2\n', 'line3\n']

f.writelines(lines)
f.close()


# Using loop :-
for i in range(5):
    f.writelines(f"Line {i+1}\n")
    f.close() 


