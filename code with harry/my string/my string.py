name='harry'           #single cote double cote doesnt matter
friend="rohan"
anotherfriend="lovish"
# apple ="he said, \"I want to eate an apple"   [double code]
apple ="he said, \"I want to eate an apple"     #[single code]
apple ='he said \n I want to eate an apple'  # new line
apple ='he said I \'want to eate an apple'

#  multiline string [triple code]

apple='''hey i am good
how are you
feeling fine'''
# print(apple)

'''                                    #to write comment [ALT+SHIFT+A]
String Def:-
Any thing that you enclose between single or double quotation marked is consideres as string.
strings are used when working with unicode characters.
'''

print("hello",name)
print(name[0])         #string is stored as 01234 position (at index 0 1st letter is situated)
print(name[1])                                           # (at index 1 2nd letter is situated)
print(name[2])                                           # (at index 2 3rd letter is situated)
print(name[3])                                           # (at index 3 4th letter is situated)
print(name[4])                                           # (at index 4 5th letter is situated)
# print(name[5])   Throws an error

# To print position of letter (index )
print(name.index("r"))

# Direct print whole series
    #When we know the count

print("using loop") 
for i in range(0,5):
    print(name[i])

print("Another method using loop")
    #When we dont know the count
for letter in name:     # [any word you can take eg. character,word,letter]
    print(letter)        

#To count letters in string
num=0
for character in name:
    print(character)
    num+=1
print(num)




