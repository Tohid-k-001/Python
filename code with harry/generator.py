def my_generator():
    for i in range(5000000):         #--> if we dont use the generator it takes lots of memory
        # complex computation
        yield i                    

gen=my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))     #--> if I comment the all above then again it prints 0

""" When you want it generate it and use it 
    1)As you can see, the generator function my_generator() returns a generator object, which can be used to generate the values
     in the range 0 to 4. 
    2)The next() function is used to request the next value from the generator, and the generator resumes its execution until 
     it encounters another yield statement or until it reaches the end of the function."""
for j in gen:
    print(j)
    if j==100:
        break

""" Benefits:-
    1)One of the main benefits of generators is that they allow you to generate the values (on-the-fly), rather than 
    having to create and store the entire sequence in memory"""
print(next(gen))

for j in gen:       # --> here it start from 102
    print(j)
    if j==150:
        break

    
    
    
